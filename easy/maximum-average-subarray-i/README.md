# 643. Maximum Average Subarray I

**Difficulty:** Easy

## Problem Description
Given an integer array `nums` and integer `k`, find the contiguous subarray of length `k` with the maximum average value and return it.

## Examples

### Example 1
```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
```

### Example 2
```
Input: nums = [5], k = 1
Output: 5.00000
```

## Constraints
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Approach
Sliding window of size `k`: compute initial sum, then slide by adding the next element and removing the leftmost. Track the max sum, divide by `k` at the end.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
