# spador

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = collections.deque()

        fresh = 0       # total number of fresh oranges
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    queue.append((r, c))
                    fresh -= 1
            time += 1
        return -1 if fresh else time
