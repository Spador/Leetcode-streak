# spador

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        origin = False # (0, 0)

        # mark start of each row and col with 0 if needed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r == 0:
                        origin = True
                    else:
                        matrix[r][0] = 0

        # converting all to 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # now changing the 0th row and 0th col
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if origin:
            for c in range(cols):
                matrix[0][c] = 0
