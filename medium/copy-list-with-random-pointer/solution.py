##spador
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldCopy = { None: None}
        current = head
        while current:
            copy = Node(current.val)
            oldCopy[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = oldCopy[current]
            copy.next = oldCopy[current.next]
            copy.random = oldCopy[current.random]
            current = current.next
        
        return oldCopy[head]
