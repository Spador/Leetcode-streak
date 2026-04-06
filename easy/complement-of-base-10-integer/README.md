# Complement of Base 10 Integer

Return the complement of an integer by flipping all bits in its binary representation.

## Approach
- Handle n = 0 as a special case (complement is 1)
- Use a bit mask starting at 1, XOR each bit position with the number to flip it
- Shift the mask left and the number right until all bits are processed

Time Complexity: O(log n)
Space Complexity: O(1)
