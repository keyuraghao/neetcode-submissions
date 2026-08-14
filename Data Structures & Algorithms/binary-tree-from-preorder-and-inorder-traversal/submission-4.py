# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder traversal 1st node is the root node
        # search this root node in the inorder traversal list. this is the partition between the left and the right sub tree
        # continue this till you hit the end of the preorder tree
        # preorder tree (node.val -> node.left.val -> node.right.val)
        # inorder tree (node.left.val -> node.val -> node.right.val)
        # time O(n^2) worst , O(n log n) best
        # space O(n)

        # if not preorder or not inorder :
            # return None
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])
        # root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # return root


        # follwing is the optimised solution Time O(n) ans space O(n)
        hashmap = {val:i for i,val in enumerate(inorder)}
        self.pre = 0

        def build(left,right):
            if left > right:
                return None
            root_val = preorder[self.pre]
            self.pre += 1
            root = TreeNode(root_val)
            mid = hashmap[root_val]
            root.left = build(left,mid-1)
            root.right = build(mid+1,right)
            return root
        return build(0,len(inorder)-1)