from typing import List
import heapq

# spador

# Time complexity: O(n^2logn)


class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)


        visit = set()

        minHeap = [[grid[0][0], 0, 0]]            # (max(height along the path/time), row, col)

        visit.add((0, 0))

        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # to iterate in 4 directions at any cell

        while minHeap:

            time, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:

                return time



            for dr, dc in dir:

                row = r + dr

                col = c + dc

                if (row < 0 or row == n or col < 0 or col == n or (row, col) in visit):

                    continue

                visit.add((row, col))

                heapq.heappush(minHeap, [max(time, grid[row][col]), row, col])
