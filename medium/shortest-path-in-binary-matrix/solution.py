# spador

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque([(0, 0, 1)]) #(row, col, distance)
        visited = set((0, 0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        while queue:
            row, col, dist = queue.popleft()
            if (row < 0 or row >= n or col < 0 or col >= n or grid[row][col] == 1):
                continue
            if row == n-1 and col == n-1:
                return dist
            
            for r, c in directions:
                if (row + r, col + c) not in visited:
                    queue.append((row + r, col + c, dist + 1))
                    visited.add((row + r, col + c))
        return -1
