# Number of 1 Bits

Count the number of set bits (1s) in a positive integer's binary representation.

## Approach
- Use bit manipulation:
  - Right shift number and check least significant bit
  - Add 1 to result if bit is set
  - Continue until number becomes 0

Time Complexity: O(log n)
Space Complexity: O(1) 