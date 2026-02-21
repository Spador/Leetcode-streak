# 268. Missing Number

**Difficulty:** Easy

## Problem Description
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing.

## Examples

### Example 1
```
Input: nums = [3,0,1]
Output: 2
```

### Example 2
```
Input: nums = [0,1]
Output: 2
```

### Example 3
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

## Constraints
- `n == nums.length`
- `1 <= n <= 10^4`
- `0 <= nums[i] <= n`
- All numbers are unique.

## Approach
Gauss formula:
1. Compute the expected sum of `[0, n]` using `n * (n + 1) / 2`.
2. Subtract every element in `nums` from that total.
3. The remainder is the missing number.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
