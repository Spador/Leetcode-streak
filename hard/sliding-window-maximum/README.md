# Sliding Window Maximum

Return the maximum value in each sliding window of size k.

## Approach
- Use a monotonic decreasing deque storing indices
- For each new element, pop from the back while the back element is smaller (it can never be the max)
- Pop from the front if the front index has fallen outside the window
- Once the window reaches size k, the front of the deque is the current maximum

Time Complexity: O(n)
Space Complexity: O(k)
