# Search a 2D Matrix II

Search for a target in an m x n matrix where rows and columns are both sorted in ascending order.

## Approach
- Start from the top-right corner
- If current value equals target, return True
- If current value is greater than target, move left (eliminate column)
- If current value is less than target, move down (eliminate row)
- Return False if out of bounds

Time Complexity: O(m + n)
Space Complexity: O(1)
