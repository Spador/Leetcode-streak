# Maximal Square

Find the largest square containing only 1s in a binary matrix and return its area.

## Approach 1: Top-Down DP (Memoization)
- Recursively compute the largest square with top-left corner at (row, col)
- Result = 1 + min(down, right, diagonal) if cell is '1', else 0
- Cache results to avoid recomputation; answer is max(cache.values())²

## Approach 2: Bottom-Up DP
- Fill a DP table from bottom-right to top-left
- dp[r][c] = largest square side with top-left at (r, c)
- dp[r][c] = 1 + min(dp[r+1][c], dp[r][c+1], dp[r+1][c+1]) if cell is '1'
- Track max side length and return its square

Time Complexity: O(m * n)
Space Complexity: O(m * n)
