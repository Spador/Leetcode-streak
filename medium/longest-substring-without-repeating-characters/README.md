# 3. Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the longest substring without duplicate characters.

## Examples

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Approach

The solution uses the **sliding window technique** with a hash set:

1. Use two pointers (`left` and `right`) to maintain a window
2. Use a set (`charSet`) to track characters in the current window
3. Expand the window by moving `right` pointer
4. When a duplicate character is found, shrink the window from the left until the duplicate is removed
5. Keep track of the maximum window size encountered

## Time Complexity

O(n) - Each character is visited at most twice (once by right pointer, once by left pointer).

## Space Complexity

O(min(m, n)) where m is the size of the character set and n is the length of the string. 