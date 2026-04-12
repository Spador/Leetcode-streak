# Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.

## Approach 1: Min-Heap
- Maintain a regular stack and a min-heap in parallel
- On push: append to stack and heappush to min-heap
- On pop: remove from stack and remove the value from the heap, then re-heapify
- getMin returns the root of the min-heap

Time Complexity: O(1) for push/top/getMin, O(n) for pop (due to heap removal)
Space Complexity: O(n)

## Approach 2: Parallel Min Stack
- Maintain a regular stack and a dedicated min stack in parallel
- On push: push val to stack; push min(val, minstack top) to minstack
- On pop: pop from both stacks simultaneously
- getMin returns the top of the min stack

Time Complexity: O(1) for all operations
Space Complexity: O(n)
