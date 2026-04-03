# Find the Index of the First Occurrence in a String

Return the index of the first occurrence of needle in haystack, or -1 if not found.

## Approach
- Use a sliding window of size len(needle) over haystack
- At each position compare the window substring against needle
- Return the left pointer index on a match, -1 if no match found

Time Complexity: O(n * m)
Space Complexity: O(1)
