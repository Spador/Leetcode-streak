##Spador

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def outOfBounds(r, c):
            return r < 0 or c < 0 or r == rows or c == cols

        areaMap = defaultdict(int)
        label = 2

        def dfs(r, c, label):
            if outOfBounds(r, c) or grid[r][c] != 1:
                return 0
            grid[r][c] = label
            size = 1
            for dr, dc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                size += dfs(dr, dc, label)
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    areaMap[label] = dfs(r, c, label)
                    label += 1

        def connect(r, c):
            visit = set()
            area = 1
            for dr, dc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if not outOfBounds(dr, dc) and grid[dr][dc] not in visit and grid[dr][dc] != 0:
                    area += areaMap[grid[dr][dc]]
                    visit.add(grid[dr][dc])
            return area

        maxArea = 0 if not areaMap else max(areaMap.values())
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    maxArea = max(maxArea, connect(r, c))

        return maxArea
