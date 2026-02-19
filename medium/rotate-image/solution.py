# spador

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0]) - 1

        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                temp = matrix[top][left + i]

                # bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                #bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                #top right to bottom left
                matrix[bottom][right - i] = matrix[top + i][right]

                #top left (temp) to top right
                matrix[top + i][right] = temp
            left += 1
            right -= 1
