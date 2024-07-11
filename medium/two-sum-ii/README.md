# Two Sum II - Input Array Is Sorted

Find two numbers in a sorted array that add up to a target value.

## Approach
- Two-pointer approach (main solution):
  - Use left and right pointers
  - Move pointers based on sum comparison with target
  - Return 1-indexed positions when sum equals target

- Binary search approach (alternative):
  - For each number, binary search for complement
  - Less efficient than two-pointer approach

Time Complexity: O(n) for two-pointer, O(n log n) for binary search
Space Complexity: O(1) 