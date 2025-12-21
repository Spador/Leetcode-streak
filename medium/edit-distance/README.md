# 72. Edit Distance

**Difficulty:** Medium

## Problem Description
Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2`.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

## Examples

### Example 1
```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

### Example 2
```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Constraints
- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Approach
1. Use dynamic programming with a 2D table where `dp[i][j]` represents the minimum number of operations required to convert `word1[i:]` to `word2[j:]`.
2. Base cases:
   - If we've reached the end of `word1` (`i == len(word1)`), we need to insert all remaining characters from `word2`: `dp[len(word1)][j] = len(word2) - j`.
   - If we've reached the end of `word2` (`j == len(word2)`), we need to delete all remaining characters from `word1`: `dp[i][len(word2)] = len(word1) - i`.
3. For each position `(i, j)`:
   - If `word1[i] == word2[j]`: no operation needed, `dp[i][j] = dp[i+1][j+1]`.
   - If `word1[i] != word2[j]`: we have three choices:
     - **Replace**: `dp[i+1][j+1]` - replace `word1[i]` with `word2[j]`.
     - **Insert**: `dp[i][j+1]` - insert `word2[j]` before `word1[i]`.
     - **Delete**: `dp[i+1][j]` - delete `word1[i]`.
     - Take the minimum of these three options and add 1 (for the operation).

## Algorithm
- Create a 2D DP table of size `(len(word1) + 1) x (len(word2) + 1)`, initialized with `float("inf")`.
- Fill base cases:
  - For `i` from `0` to `len(word1)`: `dp[i][len(word2)] = len(word1) - i`.
  - For `j` from `0` to `len(word2)`: `dp[len(word1)][j] = len(word2) - j`.
- Iterate backwards from `i = len(word1) - 1` to `0` and `j = len(word2) - 1` to `0`:
  - If `word1[i] == word2[j]`: `dp[i][j] = dp[i+1][j+1]`.
  - Else: `dp[i][j] = 1 + min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])`.
- Return `dp[0][0]`.

## Time & Space Complexity
- **Time Complexity:** `O(m * n)` where `m = len(word1)` and `n = len(word2)`. We visit each cell in the DP table once.
- **Space Complexity:** `O(m * n)` for the 2D DP table. Can be optimized to `O(min(m, n))` using space optimization.
