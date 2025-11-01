# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # Search for the node to delete
        if key > root.val:
            # Key is in right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # Key is in left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            # Node found - handle deletion
            # Case 1: Node has no left child
            if not root.left:
                return root.right
            # Case 2: Node has no right child
            elif not root.right:
                return root.left
            
            # Case 3: Node has both children
            # Find the minimum value in right subtree (inorder successor)
            curr = root.right
            while curr.left:
                curr = curr.left
            
            # Replace root value with successor value
            root.val = curr.val
            
            # Delete the successor from right subtree
            root.right = self.deleteNode(root.right, root.val)
        
        return root
