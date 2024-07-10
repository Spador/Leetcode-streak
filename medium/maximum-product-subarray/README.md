# Maximum Product Subarray

Find a subarray with the largest product in an integer array.

## Approach
- Keep track of current minimum and maximum products
- For each number, update both min and max considering:
  - Current number
  - Current number * previous max
  - Current number * previous min
- Update result with maximum product found

Time Complexity: O(n)
Space Complexity: O(1) 