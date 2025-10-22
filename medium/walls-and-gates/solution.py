import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        rows = len(rooms)
        cols = len(rooms[0])

        q = collections.deque()
        visited = set()

        def addRoom(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or rooms[r][c] == -1:
                return
            q.append([r, c])
            visited.add((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    visited.add((r, c))
                    q.append([r, c])
        dist = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                rooms[row][col] = dist
                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)
            dist += 1
