# 567. Permutation in String

## Problem Description

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

## Examples

### Example 1:
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

### Example 2:
```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Approach

The solution uses the **sliding window technique** with frequency maps:

1. **Early Return**: If `s1` is longer than `s2`, return `false`
2. **Initialize Frequency Maps**: Create maps for all 26 lowercase letters for both strings
3. **Count s1 Frequencies**: Populate the frequency map for `s1`
4. **Build Initial Window**: Count frequencies for the first `len(s1)` characters in `s2`
5. **Count Matches**: Track how many letters have matching frequencies
6. **Slide Window**: 
   - Expand window by moving right pointer
   - Shrink window by moving left pointer
   - Update match count accordingly
7. **Check for Permutation**: Return `true` if all 26 letters match in frequency

**Key Insight**: A permutation means the same characters with the same frequencies, so we track frequency matches for all possible characters.

## Time Complexity

O(n) where n is the length of `s2` - Single pass with sliding window.

## Space Complexity

O(1) - Fixed size frequency maps for 26 lowercase letters.
