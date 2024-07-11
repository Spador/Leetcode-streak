# Find Minimum in Rotated Sorted Array

Find the minimum element in a rotated sorted array of unique elements.

## Approach
- Use binary search to find the minimum element
- If left element is less than right, array is sorted
- Compare middle element with left to determine search direction
- Keep track of minimum element found

Time Complexity: O(log n)
Space Complexity: O(1) 