# 76. Minimum Window Substring

**Difficulty:** Hard

## Problem Description
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

The testcases are generated such that the answer is unique.

## Examples

### Example 1
```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

### Example 2
```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

### Example 3
```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

## Constraints
- `m == s.length`
- `n == t.length`
- `1 <= m, n <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

## Approach
We use a **sliding window** with two pointers and frequency maps to find the smallest substring of `s` that covers all characters in `t` (including duplicates).

1. Build a frequency map `countT` for all characters in `t`.
2. Maintain a window frequency map `window` for the current window in `s`.
3. Track:
   - `need` = number of distinct characters in `t` that must be satisfied.
   - `have` = number of distinct characters for which the current window meets the required frequency.
4. Slide a right pointer `right` over `s`:
   - Add `s[right]` to `window`.
   - If `s[right]` is in `countT` and `window[ch]` equals `countT[ch]`, increment `have`.
5. When `have == need`, the current window is valid; try to **shrink** from the left to find the minimum window:
   - While `have == need`:
     - Update the best (smallest) window if the current one is smaller.
     - Decrease the count of `s[left]` in `window` and move `left` forward.
     - If `s[left]` was a required character and its count in `window` falls below `countT`, decrement `have`.
6. At the end, if we found a valid window, return the substring corresponding to the best window; otherwise, return `""`.

## Time & Space Complexity
- **Time Complexity:** `O(m + n)`, where `m = len(s)` and `n = len(t)`, since each character is processed a constant number of times.
- **Space Complexity:** `O(1)` or `O(k)` where `k` is the character set size (bounded by the number of distinct letters), for the frequency maps.
