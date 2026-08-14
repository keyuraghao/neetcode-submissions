from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        ans = []
        while q:
            level_size = len(q)
            curr = []

            for _ in range(level_size):
                node = q.popleft()
                if node:
                    curr.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            ans.append(curr)
        return ans