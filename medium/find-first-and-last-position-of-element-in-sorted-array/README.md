# 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium

## Problem Description
Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

### Example 1
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### Example 3
```
Input: nums = [], target = 0
Output: [-1,-1]
```

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Approach
We need `O(log n)` time, so we use binary search. To find both the first and last positions of `target`, we run **two modified binary searches**:

1. **First occurrence** (`leftFlag = True`):
   - Standard binary search on `nums`.
   - When `nums[mid] == target`, record `pos = mid`, then continue searching **left** (`right = mid - 1`) to find an earlier occurrence.
2. **Last occurrence** (`leftFlag = False`):
   - Similar binary search.
   - When `nums[mid] == target`, record `pos = mid`, then continue searching **right** (`left = mid + 1`) to find a later occurrence.

If `target` is never found, the helper returns `-1`.

## Algorithm
- Define a helper `binSearch(nums, target, leftFlag)`:
  - Initialize `left = 0`, `right = len(nums) - 1`, `pos = -1`.
  - While `left <= right`:
    - `mid = (left + right) // 2`.
    - If `nums[mid] > target`: move left side: `right = mid - 1`.
    - Else if `nums[mid] < target`: move right side: `left = mid + 1`.
    - Else (`nums[mid] == target`):
      - Set `pos = mid`.
      - If `leftFlag` is `True`, search left: `right = mid - 1`.
      - Otherwise, search right: `left = mid + 1`.
  - Return `pos`.
- In `searchRange`:
  - `start = binSearch(nums, target, True)`
  - `last  = binSearch(nums, target, False)`
  - Return `[start, last]`.

## Time & Space Complexity
- **Time Complexity:** `O(log n)` for each binary search, `O(log n)` overall.
- **Space Complexity:** `O(1)` extra space.

