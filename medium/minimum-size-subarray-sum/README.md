# 209. Minimum Size Subarray Sum

**Difficulty:** Medium

## Problem Description
Given a positive integer `target` and an array `nums`, return the minimal length of a subarray whose sum is >= `target`. Return 0 if no such subarray exists.

## Examples

### Example 1
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
```

### Example 2
```
Input: target = 4, nums = [1,4,4]
Output: 1
```

### Example 3
```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Constraints
- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Approach
Sliding window: expand `right`, shrink from `left` whenever `currSum >= target`, updating the minimum length each time.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
