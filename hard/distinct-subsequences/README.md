# Distinct Subsequences

Return the number of distinct subsequences of s that equal t.

## Approach 1 (Top-Down DP)
- Memoized DFS where dfs(i, j) = number of ways to form t[j:] from s[i:]
- If s[i] == t[j]: branch into using or skipping s[i]; otherwise skip s[i]
- Early exit if remaining s is shorter than remaining t

## Approach 2 (Bottom-Up DP)
- Build a 2D DP table where dp[i][j] = number of ways to form t[j:] from s[i:]
- Base case: dp[r][len(t)] = 1 (empty t is always matched)
- If s[i] == t[j]: dp[i][j] = dp[i+1][j+1] + dp[i+1][j] (use or skip s[i])
- If s[i] != t[j]: dp[i][j] = dp[i+1][j] (must skip s[i])
- Answer is dp[0][0]

Time Complexity: O(m * n)
Space Complexity: O(m * n)
