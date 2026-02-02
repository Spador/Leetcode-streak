# 32. Longest Valid Parentheses

**Difficulty:** Hard

## Problem Description
Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

## Examples

### Example 1
```
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
```

### Example 2
```
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
```

### Example 3
```
Input: s = ""
Output: 0
```

## Constraints
- `0 <= s.length <= 3 * 10^4`
- `s[i]` is `'('` or `')'`.

## Approach
We use two linear scans with counters to track potential well-formed substrings without extra stack memory.

### Left-to-right scan
- Initialize `lcount = 0`, `rcount = 0`, `result = 0`.
- For each character from left to right:
  - If `'('`, increment `lcount`.
  - If `')'`, increment `rcount`.
  - If `lcount == rcount`, we found a valid substring of length `lcount + rcount`, update `result`.
  - If `rcount > lcount`, reset both counters to 0 (more right parentheses than left makes future extensions invalid).

### Right-to-left scan
To catch cases where there are more `'('` than `')'` on the left side (which the first scan can miss), repeat the logic scanning from right to left:
- Reset `lcount = 0`, `rcount = 0`.
- For each character from right to left:
  - If `'('`, increment `lcount`.
  - If `')'`, increment `rcount`.
  - If `lcount == rcount`, update `result` again.
  - If `lcount > rcount`, reset both counters to 0.

The maximum length seen across both scans is the answer.

## Time & Space Complexity
- **Time Complexity:** `O(n)` for two linear scans.
- **Space Complexity:** `O(1)` extra space.
