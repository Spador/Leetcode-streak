# 5. Longest Palindromic Substring

**Difficulty:** Medium

## Problem Description
Given a string `s`, return the longest palindromic substring in `s`.

## Examples

### Example 1
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2
```
Input: s = "cbbd"
Output: "bb"
```

## Constraints
- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters

## Approach
1. Use the expand around center technique to find palindromes.
2. For each position in the string, expand both odd-length and even-length palindromes.
3. For odd-length palindromes, start with the same center position (i, i).
4. For even-length palindromes, start with adjacent positions (i, i+1).
5. Expand outward while characters match, keeping track of the longest palindrome found.
6. Update the result whenever a longer palindrome is discovered.

## Algorithm
- Initialize `result = ""` and `resLen = 0` to track the longest palindrome.
- For each index `i` in the string:
  - **Odd palindrome**: Set `left = i, right = i` and expand while `s[left] == s[right]`.
  - **Even palindrome**: Set `left = i, right = i + 1` and expand while `s[left] == s[right]`.
  - For each expansion, if the current palindrome length exceeds `resLen`, update both `result` and `resLen`.
- Return the longest palindrome found.

## Time & Space Complexity
- **Time Complexity:** `O(n²)` - for each of n positions, we may expand up to n/2 characters in each direction.
- **Space Complexity:** `O(1)` - only using a few variables to track the result.
