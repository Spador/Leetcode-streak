# spador

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])

        queue = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            tempq = collections.deque()

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or r == rows or c < 0 or c == cols or rooms[r][c] != 2147483647:
                        continue

                    rooms[r][c] = rooms[row][col] + 1
                    tempq.append((r,c))
            queue = tempq
