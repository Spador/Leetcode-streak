# spador

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        stack = [root.val]

        # make the left boundary excluding leaf nodes
        def leftBoundary(node):
            while node:
                if node.left or node.right:
                    stack.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right
       
        # make the bottom boundary with leaf nodes from left to right
        def leafNodes(node):
            if not node.left and not node.right:
                stack.append(node.val)
                return
            if node.left:
                leafNodes(node.left)
            if node.right:
                leafNodes(node.right)
        
        # make the right boundary in reverse excluding leaf nodes
        tempstack = []
        
        def rightBoundary(node):
            while node:
                if node.left or node.right:
                    tempstack.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
        
        leftBoundary(root.left)
        leafNodes(root)
        rightBoundary(root.right)

        while tempstack:
            stack.append(tempstack.pop())
        return stack
