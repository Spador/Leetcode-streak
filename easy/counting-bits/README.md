# Counting Bits

Return an array where each element represents the number of 1's in the binary representation of its index.

## Approach
- Use dynamic programming with pattern recognition
- For each number i:
  - If i is a power of 2, update offset
  - Number of 1's = 1 + number of 1's in (i - offset)
- Pattern: Each power of 2 starts a new sequence

Time Complexity: O(n)
Space Complexity: O(n) 