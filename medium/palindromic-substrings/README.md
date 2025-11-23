# 647. Palindromic Substrings

**Difficulty:** Medium

## Problem Description
Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

## Examples

### Example 1
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

### Example 2
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters

## Approach
1. Use the expand around center technique similar to finding the longest palindromic substring.
2. For each position in the string, expand both odd-length and even-length palindromes.
3. For odd-length palindromes, start with the same center position (i, i).
4. For even-length palindromes, start with adjacent positions (i, i+1).
5. Expand outward while characters match, incrementing a counter for each valid palindrome found.
6. Return the total count of all palindromic substrings.

## Algorithm
- Initialize `result = 0` to count palindromic substrings.
- For each index `i` in the string:
  - **Odd palindrome**: Set `left = i, right = i` and expand while `s[left] == s[right]`. For each valid expansion, increment `result`.
  - **Even palindrome**: Set `left = i, right = i + 1` and expand while `s[left] == s[right]`. For each valid expansion, increment `result`.
- Return the total count.

## Time & Space Complexity
- **Time Complexity:** `O(n²)` - for each of n positions, we may expand up to n/2 characters in each direction.
- **Space Complexity:** `O(1)` - only using a counter variable.
