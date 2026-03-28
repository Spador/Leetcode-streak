# 16. 3Sum Closest

**Difficulty:** Medium

## Problem Description
Given an integer array `nums` and a `target`, find three integers whose sum is closest to `target` and return that sum.

## Examples

### Example 1
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
```

### Example 2
```
Input: nums = [0,0,0], target = 1
Output: 0
```

## Constraints
- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## Approach
Sort + two pointers:
1. Fix one element, use two pointers for the remaining pair.
2. Track the closest sum seen so far.
3. Return early if exact match found.

## Time & Space Complexity
- **Time Complexity:** `O(n^2)`
- **Space Complexity:** `O(1)`
