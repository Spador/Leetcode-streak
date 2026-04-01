# 696. Count Binary Substrings

**Difficulty:** Easy

## Problem Description
Given a binary string `s`, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

## Examples

### Example 1
```
Input: s = "00110011"
Output: 6
```

### Example 2
```
Input: s = "10101"
Output: 4
```

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

## Approach
Track the current run streak (`strk`) and the previous run streak (`prev`). Whenever the character changes, update `prev = strk` and reset `strk = 1`. If `strk <= prev`, a valid grouped substring exists at this boundary, so increment result.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
