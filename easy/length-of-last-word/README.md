# Length of Last Word

Return the length of the last word in a string that may have trailing spaces.

## Approach
- First pass from the right: skip trailing spaces to find the true end of the last word
- Second pass from that position backwards: count characters until a space or the start is reached

Time Complexity: O(n)
Space Complexity: O(1)
