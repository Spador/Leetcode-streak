# Longest Common Prefix

Find the longest common prefix string amongst an array of strings.

## Approach
- Sort array to get lexicographically first and last strings
- Compare characters at same positions in first and last strings
- Build prefix until characters differ

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) 