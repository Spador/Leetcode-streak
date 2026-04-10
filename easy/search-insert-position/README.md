# Search Insert Position

Given a sorted array and a target, return the index of the target or the index where it would be inserted.

## Approach
- Standard binary search; narrow left/right based on comparison with mid
- If target is found return mid immediately
- When the loop ends, left points to the correct insertion position

Time Complexity: O(log n)
Space Complexity: O(1)
