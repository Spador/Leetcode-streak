# 215. Kth Largest Element in an Array

## Problem Description

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

## Examples

### Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

### Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Approach

- Use a max-heap to efficiently find the kth largest element
- Since Python's heapq is a min-heap, negate all values to simulate max-heap behavior
- Convert the array to a heap using heapify
- Extract k elements from the heap, with the kth extraction being our answer
- Return the absolute value of the kth extracted element

## Time and Space Complexity

- **Time Complexity**: O(n + k log n) where n is the length of nums
  - O(n) for heapify operation to build the heap
  - O(k log n) for extracting k elements from the heap
- **Space Complexity**: O(1) extra space (not counting the input array)
  - We modify the input array in-place

## Difficulty
Medium
