# 91. Decode Ways

**Difficulty:** Medium

## Problem Description
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

- "1" -> 'A'
- "2" -> 'B'
- ...
- "25" -> 'Y'
- "26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:
- "AAJF" with the grouping (1, 1, 10, 6)
- "KJF" with the grouping (11, 10, 6)

The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).

Note: there may be strings that are impossible to decode.

Given a string `s` containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

## Examples

### Example 1
```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

### Example 2
```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

### Example 3
```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.
```

## Constraints
- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zero(s)

## Approach
1. This is a dynamic programming problem where we need to count the number of ways to decode a string.
2. For each position, we can either:
   - Decode a single digit (1-9, excluding 0)
   - Decode two digits together (10-26, where the first digit is 1 or 2, and if 2, the second digit must be 0-6)
3. Use memoization (top-down) or tabulation (bottom-up) to avoid recalculating subproblems.
4. Base case: an empty string has 1 way to decode (successfully completed).
5. Invalid cases: if a digit is '0', it cannot be decoded alone (must be part of 10 or 20).

## Algorithm

### Top-Down Approach (Recursive with Memoization)
- Use a dictionary `dp` to memoize results, with `dp[len(s)] = 1` as base case.
- For each position `i`:
  - If `s[i] == "0"`, return 0 (invalid single digit).
  - Start with `result = dfs(i+1)` (decode single digit).
  - If two digits form a valid code (10-26), add `dfs(i+2)` to result.
- Return the memoized result.

### Bottom-Up Approach (Iterative)
- Initialize `dp[len(s)] = 1` as base case.
- Iterate backwards from `len(s)-1` to `0`:
  - If `s[i] == "0"`, set `dp[i] = 0`.
  - Otherwise, start with `dp[i] = dp[i+1]` (single digit decoding).
  - If two digits form a valid code (10-26), add `dp[i+2]` to `dp[i]`.
- Return `dp[0]`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` - we visit each position once.
- **Space Complexity:** `O(n)` - for the memoization dictionary or DP array.
