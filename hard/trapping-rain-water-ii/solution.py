# spador

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])

        minHeap = []

        # 1. Added all the border element in the min heap
        # Because this are never going to trap any water as mentioned in the question
        # All the added cells are then marked with -1 and to show visited.

        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    heapq.heappush(minHeap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1


        result = 0
        maxH = -1

        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            maxH = max(maxH, h)
            result += maxH - h

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for nr, nc in neighbors:
                if nr < 0 or nr == rows or nc < 0 or nc == cols or heightMap[nr][nc] == -1:
                    continue
                heapq.heappush(minHeap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return result
