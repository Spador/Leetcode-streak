# 1461. Check If a String Contains All Binary Codes of Size K

**Difficulty:** Medium

## Problem Description
Given a binary string `s` and an integer `k`, return `true` if **every** binary code of length `k` is a substring of `s`. Otherwise, return `false`.

## Examples

### Example 1
```
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11".
```

### Example 2
```
Input: s = "0110", k = 1
Output: true
Explanation: The binary codes of length 1 are "0" and "1".
```

### Example 3
```
Input: s = "0110", k = 2
Output: false
Explanation: The binary code "00" is of length 2 and does not exist in the string.
```

## Constraints
- `1 <= s.length <= 5 * 10^5`
- `s[i]` is either `'0'` or `'1'`
- `1 <= k <= 20`

## Approach
Slide a window of length `k` across `s` and add each substring of length `k` to a set. There are exactly `2^k` possible binary codes of length `k`. If the set size equals `2^k` (i.e. `1 << k`), then `s` contains all codes.

## Time & Space Complexity
- **Time Complexity:** O(n * k) due to substring creation (with small `k <= 20`).
- **Space Complexity:** O(2^k * k) to store all distinct substrings.
