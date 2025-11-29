# 97. Interleaving String

**Difficulty:** Medium

## Problem Description
Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an interleaving of `s1` and `s2`.

An interleaving of two strings `s` and `t` is a configuration where `s` and `t` are divided into `n` and `m` substrings respectively, such that:

- `s = s1 + s2 + ... + sn`
- `t = t1 + t2 + ... + tm`
- `|n - m| <= 1`
- The interleaving is `s1 + t1 + s2 + t2 + s3 + t3 + ...` or `t1 + s1 + t2 + s2 + t3 + s3 + ...`

Note: `a + b` is the concatenation of strings `a` and `b`.

## Examples

### Example 1
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.
```

### Example 2
```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.
```

### Example 3
```
Input: s1 = "", s2 = "", s3 = ""
Output: true
```

## Constraints
- `0 <= s1.length, s2.length <= 100`
- `0 <= s3.length <= 200`
- `s1`, `s2`, and `s3` consist of lowercase English letters

## Follow up
Could you solve it using only `O(s2.length)` additional memory space?

## Approach
1. Use dynamic programming with a 2D table where `dp[i][j]` represents whether `s3[i+j:]` can be formed by interleaving `s1[i:]` and `s2[j:]`.
2. First check if `len(s1) + len(s2) == len(s3)`, otherwise return `false`.
3. Work backwards from the end of both strings.
4. Base case: `dp[len(s1)][len(s2)] = True` (empty strings can form empty string).
5. For each position `(i, j)`, check if we can match:
   - `s1[i]` with `s3[i+j]` and `dp[i+1][j]` is `True`, OR
   - `s2[j]` with `s3[i+j]` and `dp[i][j+1]` is `True`.
6. Return `dp[0][0]` which represents whether the entire `s3` can be formed.

## Algorithm
- If `len(s1) + len(s2) != len(s3)`, return `False`.
- Create a 2D DP table of size `(len(s1) + 1) x (len(s2) + 1)`, initialized with `False`.
- Set `dp[len(s1)][len(s2)] = True` (base case).
- Iterate backwards from `i = len(s1)` to `0` and `j = len(s2)` to `0`:
  - If `i < len(s1)` and `s1[i] == s3[i+j]` and `dp[i+1][j]` is `True`, set `dp[i][j] = True`.
  - If `j < len(s2)` and `s2[j] == s3[i+j]` and `dp[i][j+1]` is `True`, set `dp[i][j] = True`.
- Return `dp[0][0]`.

## Time & Space Complexity
- **Time Complexity:** `O(n * m)` where `n = len(s1)` and `m = len(s2)` - we visit each cell in the DP table once.
- **Space Complexity:** `O(n * m)` for the 2D DP table. Can be optimized to `O(min(n, m))` using space optimization.
