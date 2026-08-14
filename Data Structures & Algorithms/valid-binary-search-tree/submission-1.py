# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # follwoing is the recursive approach Time O(n) and stack space O(n)
        # def dfs(node,low,high):
            # if not node:
                # return True
            # if not (low < node.val < high):
                # return False
            # return dfs(node.left,low,node.val) and dfs(node.right,node.val,high)
        # return dfs(root,float('-inf'),float('inf'))

        # follwoing is the iterative approach using stack:
        stack = []
        low = float('-inf')
        high = float('inf')
        stack.append((root,low,high))
        while stack:
            node,low_val, high_val = stack.pop()
            if not node:
                continue
            if not (low_val < node.val < high_val):
                return False
            stack.append((node.left,low_val,node.val))
            stack.append((node.right,node.val,high_val))
        return True
        