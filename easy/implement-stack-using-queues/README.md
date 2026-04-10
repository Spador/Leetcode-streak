# Implement Stack using Queues

Implement a LIFO stack using only a single queue's standard operations.

## Approach
- Use one deque and track size
- On push: append the new element, then rotate all previous elements to the back (size - 1 times) so the newest element is always at the front
- pop and top simply operate on the front of the deque

Time Complexity: O(n) for push, O(1) for pop/top/empty
Space Complexity: O(n)
