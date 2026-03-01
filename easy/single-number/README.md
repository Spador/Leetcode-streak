# 136. Single Number

**Difficulty:** Easy

## Problem Description
Given a non-empty array where every element appears twice except one, find the single one. Must run in `O(n)` time and `O(1)` space.

## Examples

### Example 1
```
Input: nums = [2,2,1]
Output: 1
```

### Example 2
```
Input: nums = [4,1,2,1,2]
Output: 4
```

### Example 3
```
Input: nums = [1]
Output: 1
```

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Every element appears twice except one.

## Approach
XOR all elements together. Duplicate pairs cancel out (`n ^ n = 0`) and the single number remains (`n ^ 0 = n`).

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
