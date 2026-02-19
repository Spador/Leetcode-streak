# spador

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(numRows - 1):
            prev = [0] + result[-1] + [0]
            row = []
            for j in range(len(result[-1]) + 1):
                row.append(prev[j] + prev[j+1])
            result.append(row)
        return result
