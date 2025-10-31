"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # Case 1: If node.right exists, the successor is the leftmost node in right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # Case 2: If node.right does not exist, find the first parent 
        # which has this node in its left subtree
        # If there is no such parent, it means it is the largest node in BST so return None
        while node.parent and node == node.parent.right:
            node = node.parent
        
        return node.parent
