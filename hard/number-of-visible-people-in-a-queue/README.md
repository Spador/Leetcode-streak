# Number of Visible People in a Queue

Return an array where answer[i] is the number of people person i can see to their right.

## Approach
- Traverse right to left using a monotonic decreasing stack
- For each person, pop all stack elements shorter than them (each popped person is visible) and count them
- If the stack is still non-empty after popping, the next taller person is also visible (+1)
- Push current height onto the stack

Time Complexity: O(n)
Space Complexity: O(n)
