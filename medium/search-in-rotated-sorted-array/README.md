# Search in Rotated Sorted Array

Find target in a rotated sorted array with O(log n) time complexity.

## Approach
- Use binary search with modified conditions
- Check if left half is sorted
- Determine which half to search based on target value
- Handle rotation by comparing with array bounds

Time Complexity: O(log n)
Space Complexity: O(1) 