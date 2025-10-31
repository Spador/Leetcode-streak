# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        successor = None
        
        while root:
            # Case 1: If p.val is greater than or equal to root.val,
            # the successor must be in the right subtree
            if p.val >= root.val:
                root = root.right
            else:
                # Case 2: root is a potential successor,
                # but there might be a smaller one in the left subtree
                successor = root
                root = root.left
                
        return successor
