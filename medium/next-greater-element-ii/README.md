# Next Greater Element II

For each element in a circular array, return the next greater element found by traversing in order (wrapping around).

## Approach
- Simulate the circular array by iterating indices from 2n-1 down to 0 using i % n
- Use a monotonic decreasing stack; pop elements smaller than or equal to the current
- If the stack is non-empty after popping, the top is the next greater element for this index
- Iterating right to left ensures stack already contains elements that appear later in traversal order

Time Complexity: O(n)
Space Complexity: O(n)
