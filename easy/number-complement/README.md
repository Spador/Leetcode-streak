# Number Complement

Return the complement of an integer by flipping all bits in its binary representation.

## Approach
- Use a bit mask starting at 1, XOR each bit position with the number to flip it
- Shift the mask left and the number right until all bits are processed

Time Complexity: O(log n)
Space Complexity: O(1)
