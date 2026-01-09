# spador

from collections import deque, defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])             # List of tuples (node, col)
        minCol, maxCol = 0 , 0          # Keep track of min and max column to iterate
        colMap = defaultdict(list)      # Key: Col -> Val: all the nodes at that column

        while queue:
            node, col = queue.popleft()
            minCol, maxCol = min(minCol, col), max(maxCol, col)

            colMap[col].append(node.val)
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        return [colMap[c] for c in range(minCol, maxCol + 1)]


