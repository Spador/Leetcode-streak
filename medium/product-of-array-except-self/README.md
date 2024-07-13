# Product of Array Except Self

Return an array where each element is the product of all elements in the input array except the current element.

## Approach
- Use two passes:
  - First pass: Calculate prefix products
  - Second pass: Multiply with postfix products
- Avoid division by using prefix and postfix arrays
- Optimize space by using output array for both passes

Time Complexity: O(n)
Space Complexity: O(1) excluding output array 