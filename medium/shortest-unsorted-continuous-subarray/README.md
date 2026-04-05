# Shortest Unsorted Continuous Subarray

Find the length of the shortest subarray that, when sorted, makes the whole array sorted.

## Approach
- Traverse left to right tracking the running maximum; whenever an element is less than the current max, update the right boundary
- Traverse right to left tracking the running minimum; whenever an element is greater than the current min, update the left boundary
- The answer is right - left + 1, or 0 if the array is already sorted

Time Complexity: O(n)
Space Complexity: O(1)
