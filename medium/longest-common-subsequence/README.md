# 1143. Longest Common Subsequence

**Difficulty:** Medium

## Problem Description
Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

## Examples

### Example 1
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

### Example 2
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

### Example 3
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

## Constraints
- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters

## Approach
1. Use dynamic programming with a 2D table where `dp[i][j]` represents the length of the longest common subsequence between `text1[i:]` and `text2[j:]`.
2. Work backwards from the end of both strings to the beginning.
3. For each position `(i, j)`:
   - If `text1[i] == text2[j]`, the characters match, so we can extend the LCS: `dp[i][j] = 1 + dp[i+1][j+1]`.
   - If the characters don't match, take the maximum of:
     - `dp[i][j+1]` (skip character in text2)
     - `dp[i+1][j]` (skip character in text1)
4. The base case is when we reach the end of either string (handled by the `+1` padding in the DP table).
5. Return `dp[0][0]` which represents the LCS of the entire strings.

## Algorithm
- Create a 2D DP table of size `(len(text1) + 1) x (len(text2) + 1)`, initialized with zeros.
- Iterate backwards from `i = len(text1) - 1` to `0`:
  - For each `i`, iterate backwards from `j = len(text2) - 1` to `0`:
    - If `text1[i] == text2[j]`: `dp[i][j] = 1 + dp[i+1][j+1]`.
    - Else: `dp[i][j] = max(dp[i][j+1], dp[i+1][j])`.
- Return `dp[0][0]`.

## Time & Space Complexity
- **Time Complexity:** `O(m * n)` where `m` and `n` are the lengths of `text1` and `text2` respectively.
- **Space Complexity:** `O(m * n)` for the 2D DP table.
