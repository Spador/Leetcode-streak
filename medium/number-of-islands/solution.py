import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if r < rows and r >= 0 and c < cols and c >= 0 and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r,c))

        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands


# To make this approach dfs instead of bfs, just change the q.popleft() to q.pop()
