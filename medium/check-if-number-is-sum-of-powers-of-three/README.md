# Check if Number is a Sum of Powers of Three

Determine if a number can be represented as sum of distinct powers of three.

## Approach
- Convert number to base-3 representation
- Check if any digit is 2 (which would require using same power twice)
- If no digit is 2, number can be represented as sum of distinct powers
- Return true if all digits are 0 or 1

Time Complexity: O(log n)
Space Complexity: O(log n) 