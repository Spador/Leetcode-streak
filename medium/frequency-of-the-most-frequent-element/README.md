# 1838. Frequency of the Most Frequent Element

**Difficulty:** Medium

## Problem Description
Given an integer array `nums` and integer `k`, you can increment any element by 1 in one operation. Return the maximum possible frequency of any element after at most `k` operations.

## Examples

### Example 1
```
Input: nums = [1,2,4], k = 5
Output: 3
```

### Example 2
```
Input: nums = [1,4,8,13], k = 5
Output: 2
```

### Example 3
```
Input: nums = [3,9,6], k = 2
Output: 1
```

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- `1 <= k <= 10^5`

## Approach
Sort the array, then use a sliding window. The window is valid when `nums[right] * window_size <= total_sum + k` (cost to raise all elements to `nums[right]`). Shrink from left when invalid.

## Time & Space Complexity
- **Time Complexity:** `O(n log n)`
- **Space Complexity:** `O(1)`
