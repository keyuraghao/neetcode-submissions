# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            leftmax = max(leftmax,0) # because the left path can have -ve value and we dont want that
            rightmax = max(rightmax,0) # becaue the right path can have -ve value and we dont want that

            ans[0] = max(ans[0], root.val + leftmax + rightmax)

            return root.val + max(leftmax,rightmax)
        
        dfs(root)
        return ans[0]
        