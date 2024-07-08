# Group Anagrams

Group strings that are anagrams of each other.

## Approach
- Use character count as key for grouping
- Create 26-length array for each string
- Count frequency of each character
- Use tuple of counts as dictionary key

Time Complexity: O(n * k) where k is max string length
Space Complexity: O(n * k) 