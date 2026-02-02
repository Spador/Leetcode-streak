# spador

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            arr.append(node)
            inOrder(node.right)

        def balance(l ,r):
            if l > r:
                return None
            m = (l + r) // 2
            L = balance(l, m - 1)
            R = balance(m+1, r)
            arr[m].left = L
            arr[m].right = R
            return arr[m]
        
        inOrder(root)
        return balance(0, len(arr) - 1)
