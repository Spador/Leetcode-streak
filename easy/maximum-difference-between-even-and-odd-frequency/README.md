# 3442. Maximum Difference Between Even and Odd Frequency I

## Problem Description

You are given a string `s` consisting of lowercase English letters.

Your task is to find the maximum difference `diff = freq(a1) - freq(a2)` between the frequency of characters `a1` and `a2` in the string such that:

- `a1` has an **odd** frequency in the string.
- `a2` has an **even** frequency in the string.

Return this maximum difference.

## Examples

### Example 1:
```
Input: s = "aaaaabbc"
Output: 3
Explanation:
The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
The maximum difference is 5 - 2 = 3.
```

### Example 2:
```
Input: s = "abcabcab"
Output: 1
Explanation:
The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
The maximum difference is 3 - 2 = 1.
```

## Constraints

- `3 <= s.length <= 100`
- `s` consists only of lowercase English letters.
- `s` contains at least one character with an odd frequency and one with an even frequency.

## Approach

The solution uses a **frequency counting approach**:

1. **Count Frequencies**: Use a hash map to count the frequency of each character in the string
2. **Find Maximum Odd Frequency**: Iterate through all frequencies and find the maximum odd frequency
3. **Find Minimum Even Frequency**: Iterate through all frequencies and find the minimum even frequency
4. **Calculate Difference**: Return the difference between maximum odd and minimum even frequencies

**Key Insight**: We want the largest possible difference, so we need the maximum odd frequency minus the minimum even frequency.

## Time Complexity

O(n) - Single pass to count frequencies, then iterate through the frequency map.

## Space Complexity

O(1) - Hash map stores at most 26 characters (lowercase English letters).
