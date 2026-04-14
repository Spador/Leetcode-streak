# spador

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        # top-down recursion with Memoisation
        cache = {}      #(row, col) -> square length

        def square(row, col):
            if row >= rows or col >= cols:
                return 0

            if (row, col) not in cache:
                down = square(row + 1, col)
                right = square(row, col + 1)
                diag = square(row + 1, col + 1)
                cache[(row, col)] = 0
                if matrix[row][col] == "1":
                    cache[(row, col)] = 1 + min(down, right, diag)

            return cache[(row, col)]
        square(0, 0)
        return max(cache.values()) ** 2


        # bottom-up solution DP - Table

        DP = [[0] * cols for _ in range(rows)]
        maxside = 0
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if matrix[r][c] == "1":
                    if r == rows - 1 or c == cols - 1:
                        DP[r][c] = 1
                    else:
                        DP[r][c] = 1 + min(DP[r + 1][c], DP[r][c + 1], DP[r + 1][c + 1])
                else:
                    DP[r][c] = 0

                maxside = max(maxside, DP[r][c])

        return maxside**2
