# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # using DFS go to the lowest value in the tree (i.e. the left most leaf) and create a array using in order traversal (node.left -> node.val -> node.right) becaue of the bst property as we hit the length of the arr to be k return the element. Time O(n) Space O(k)

        ans = []

        # initially doing recursively
        def dfs(node):
            if not node or len(ans) > k:
                return
            if node.left:
                dfs(node.left)
            ans.append(node.val)
            if len(ans) > k:
                return
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return ans[k-1]