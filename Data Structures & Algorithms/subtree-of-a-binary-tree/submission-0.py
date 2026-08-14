# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same_tree(p,q):
            if not q and not p:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            return same_tree(p.left,q.left) and same_tree(p.right,q.right)
        
        def has_subtree(root):
            if not root:
                return False
            
            if same_tree(root,subRoot):
                return True
            
            return has_subtree(root.left) or has_subtree(root.right)
        
        return has_subtree(root)