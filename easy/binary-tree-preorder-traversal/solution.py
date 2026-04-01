# spador

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        # recursive approach
        def dfs(node):
            if not node:
                return []
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return res
        # return dfs(root)

        # iterative approach
        curr, stack = root, []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return res
