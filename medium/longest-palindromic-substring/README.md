# Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

## Approach
- Use expand around center technique
- For each position, expand both odd and even length palindromes
- Keep track of longest palindrome found

Time Complexity: O(n²)
Space Complexity: O(1) 