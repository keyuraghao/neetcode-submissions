from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q1.append(p)

        q2 = deque()
        q2.append(q)

        while q1 and q2:
            q1_level = len(q1)
            q2_level = len(q2)

            if q1_level != q2_level:
                return False
            node1 = q1.popleft()
            node2 = q2.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)

        return not q1 and not q2