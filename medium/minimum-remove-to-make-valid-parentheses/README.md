# Minimum Remove to Make Valid Parentheses

Remove minimum number of parentheses to make a string valid.

## Approach
- Use stack to track valid parentheses pairs
- Initialize result array with empty strings
- For each character:
  - Keep non-parentheses characters
  - Track opening parentheses positions
  - Match closing parentheses with opening ones
  - Only keep matched pairs in result

Time Complexity: O(n)
Space Complexity: O(n) 