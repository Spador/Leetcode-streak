# spador

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # recursive approach
        def dfs(node):
            if not node:
                return []
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)
            return result
        # return dfs(root)
        
        # iterative approach
        stack = [root]
        visit = [False]
        
        while stack:
            curr = stack.pop()
            v = visit.pop()
            if curr:
                if v:
                    result.append(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
        return result
