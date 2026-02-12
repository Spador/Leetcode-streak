# spador

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
from typing import Optional, List

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        minCol, maxCol = 0, 0
        colMap = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])

        while queue:
            node, row, col = queue.popleft()
            colMap[col].append((node.val, row))
            minCol, maxCol = min(minCol, col), max(maxCol, col)

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        result = []
        for col in range(minCol, maxCol + 1):
            colMap[col].sort(key = lambda x: (x[1], x[0]))
            items = [val for val, _ in colMap[col]]
            result.append(items)
        return result
