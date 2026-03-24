# spador

# doing the double binary search, once in the column and then in the row

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            midRow = top + ((bot - top) // 2)
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break

        if top > bot:
            return False
        row = (top + bot) // 2
        left, right = 0, cols - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False
