# 448. Find All Numbers Disappeared in an Array

**Difficulty:** Easy

## Problem Description
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return all integers in `[1, n]` that do not appear in `nums`.

## Examples

### Example 1
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
```

### Example 2
```
Input: nums = [1,1]
Output: [2]
```

## Constraints
- `n == nums.length`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= n`

## Approach
In-place index marking:
1. For each number `n` in the array, negate the value at index `abs(n) - 1` to mark it as visited.
2. After the pass, any index with a positive value means `index + 1` was never seen — collect those.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` extra (result list excluded)
