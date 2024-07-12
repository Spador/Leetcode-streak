# Contains Duplicate

Check if an array contains any duplicate values.

## Approach
- Set-based solution (main):
  - Compare length of array with length of set
  - If lengths differ, array contains duplicates

- Hash map solution (alternative):
  - Use dictionary to track seen numbers
  - Return true if number is seen twice

Time Complexity: O(n)
Space Complexity: O(n) 