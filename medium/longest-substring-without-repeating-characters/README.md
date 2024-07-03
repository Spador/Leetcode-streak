# Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

## Approach
- Use sliding window with hashmap to track character positions
- When duplicate found, move window start to position after first occurrence
- Keep track of maximum length seen so far

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is charset size 