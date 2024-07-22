# 424. Longest Repeating Character Replacement

## Problem Description

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Examples

### Example 1:
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
```

### Example 2:
```
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Approach

The solution uses the **sliding window technique** with a frequency map:

1. Use two pointers (`left` and `right`) to maintain a window
2. Keep track of character frequencies in the current window using a hash map
3. For each window, calculate the number of characters that need to be changed:
   - `(window_size - max_frequency) <= k`
4. If the condition is satisfied, expand the window by moving `right`
5. If not, shrink the window by moving `left`
6. Keep track of the maximum window size encountered

**Key Insight**: The longest valid substring will have the most frequent character repeated, with at most `k` other characters that can be changed to match it.

## Time Complexity

O(n) - Single pass through the string with sliding window.

## Space Complexity

O(1) - Hash map stores at most 26 characters (uppercase English letters).
