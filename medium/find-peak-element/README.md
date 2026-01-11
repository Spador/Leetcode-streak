# 162. Find Peak Element

**Difficulty:** Medium

## Problem Description
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

## Examples

### Example 1
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, 
or index number 5 where the peak element is 6.
```

## Constraints
- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`.

## Approach
Because we must run in `O(log n)` time, we use a **binary search** approach. The key observations are:

1. Adjacent elements are never equal and a peak is guaranteed to exist.
2. If `nums[mid] < nums[mid - 1]`, then there must be a peak on the **left** side (since we're on a downward slope when moving from `mid - 1` to `mid`).
3. If `nums[mid] < nums[mid + 1]`, then there must be a peak on the **right** side (since we're on an upward slope when moving from `mid` to `mid + 1`).
4. Otherwise, `nums[mid]` is greater than or equal to both neighbors (or is at a boundary), so `mid` is a peak.

## Algorithm
- Initialize `left = 0`, `right = len(nums) - 1`.
- While `left <= right`:
  - Compute `mid = left + (right - left) // 2`.
  - If `mid > 0` and `nums[mid] < nums[mid - 1]`, move left: `right = mid - 1`.
  - Else if `mid < len(nums) - 1` and `nums[mid] < nums[mid + 1]`, move right: `left = mid + 1`.
  - Otherwise, return `mid` (we found a peak).

This strategy always moves towards a direction where a peak is guaranteed to exist.

## Time & Space Complexity
- **Time Complexity:** `O(log n)` due to binary search.
- **Space Complexity:** `O(1)` additional space.

