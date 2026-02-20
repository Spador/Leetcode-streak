# 485. Max Consecutive Ones

**Difficulty:** Easy

## Problem Description
Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

## Examples

### Example 1
```
Input: nums = [1,1,0,1,1,1]
Output: 3
```

### Example 2
```
Input: nums = [1,0,1,1,0,1]
Output: 2
```

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`

## Approach
1. Track a running count `currMax` of consecutive 1s.
2. On each `1`, increment `currMax` and update `result` if it's a new max.
3. On each `0`, reset `currMax` to 0.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — single pass through the array.
- **Space Complexity:** `O(1)` — only two counters used.
