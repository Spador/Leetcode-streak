# 115. Distinct Subsequences

**Difficulty:** Hard

## Problem Description
Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

The test cases are generated so that the answer fits on a 32-bit signed integer.

## Examples

### Example 1
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

### Example 2
```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```

## Constraints
- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.

## Approach
1. Use dynamic programming with memoization (top-down approach).
2. For each position `(i, j)` where `i` is the index in `s` and `j` is the index in `t`, compute the number of distinct subsequences of `s[i:]` that equal `t[j:]`.
3. Use a dictionary `dp` to cache results and avoid redundant calculations.
4. Base cases:
   - If `j == len(t)`, we've matched all characters in `t`, return `1` (one valid subsequence found).
   - If `i >= len(s)` or there aren't enough remaining characters in `s` to match the rest of `t`, return `0`.
5. For each position:
   - If `s[i] == t[j]`, we have two choices:
     - Use `s[i]` to match `t[j]`: recurse to `dfs(i+1, j+1)`.
     - Skip `s[i]` and try to match `t[j]` later: recurse to `dfs(i+1, j)`.
     - The total is the sum of both choices.
   - If `s[i] != t[j]`, we can only skip `s[i]`: recurse to `dfs(i+1, j)`.

## Algorithm
- Initialize an empty dictionary `dp` to cache results.
- Define a recursive function `dfs(i, j)`:
  - If `j == len(t)`: return `1` (base case - all characters matched).
  - If `i >= len(s)` or `len(t) - j > len(s) - i`: return `0` (impossible to match).
  - If `(i, j)` is in `dp`: return the cached value.
  - If `s[i] == t[j]`:
    - `dp[(i, j)] = dfs(i+1, j+1) + dfs(i+1, j)` (use current character + skip current character).
  - Else:
    - `dp[(i, j)] = dfs(i+1, j)` (skip current character).
  - Return `dp[(i, j)]`.
- Return `dfs(0, 0)`.

## Time & Space Complexity
- **Time Complexity:** `O(n * m)` where `n = len(s)` and `m = len(t)`. Each pair `(i, j)` is computed at most once.
- **Space Complexity:** `O(n * m)` for the `dp` dictionary and the recursion stack in the worst case.
