# 18. 4Sum

**Difficulty:** Medium

## Problem Description
Given an array `nums` and a `target`, return all unique quadruplets `[a, b, c, d]` such that their sum equals `target`.

## Examples

### Example 1
```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

### Example 2
```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

## Constraints
- `1 <= nums.length <= 200`
- `-10^9 <= nums[i], target <= 10^9`

## Approach
Generalised k-sum with recursion + two pointers:
1. Sort the array.
2. Recursively reduce k-sum to (k-1)-sum by fixing one element at a time, skipping duplicates.
3. Base case is 2-sum solved with two pointers, skipping duplicates after each match.
4. Works for any k, not just 4.

## Time & Space Complexity
- **Time Complexity:** `O(n^3)` for 4Sum
- **Space Complexity:** `O(k)` recursion depth
