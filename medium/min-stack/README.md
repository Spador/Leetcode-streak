# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.

## Approach
- Maintain a regular stack for push/pop/top operations
- Maintain a min-heap in parallel to track the minimum element
- On push: append to stack and heappush to min-heap
- On pop: remove from stack and remove the value from the heap, then re-heapify
- getMin returns the root of the min-heap

Time Complexity: O(1) for push/top/getMin, O(n) for pop (due to heap removal)
Space Complexity: O(n)
