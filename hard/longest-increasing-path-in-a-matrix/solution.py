# spador

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}    # Key: (r, c) -> value: max increasing
        row = len(matrix)
        col = len(matrix[0])

        def dfs(r, c, prev):
            if r >= row or r < 0 or c >= col or c < 0 or matrix[r][c] <= prev:
                return 0
            
            if (r, c) in dp:
                return dp[(r,c)]
            
            result = 1
    
            result = max(result, 1 + dfs(r + 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r - 1, c, matrix[r][c]))
            result = max(result, 1 + dfs(r, c + 1, matrix[r][c]))
            result = max(result, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = result

            return result
        
        for i in range(row):
            for j in range(col):
                dfs(i, j, -1)
        return max(dp.values())
