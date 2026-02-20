# spador

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # add the top row to the result
            for i in range(left, right):
                result.append(matrix[top][i])
            top += 1

            # add the right column to the result
            for i in range(top, bottom):
                result.append(matrix[i][right - 1])
            right -= 1

            if not (right > left and bottom > top):
                break

            # add the bottom row in reverse to result
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom - 1][i])
            bottom -= 1

            # add the left column in reverse to result
            for i in range(bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
        return result
