# 75. Sort Colors

**Difficulty:** Medium

## Problem Description
Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Use the integers `0`, `1`, and `2` to represent red, white, and blue respectively.

You must solve this problem without using the library's sort function.

## Examples

### Example 1
```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

### Example 2
```
Input: nums = [2,0,1]
Output: [0,1,2]
```

## Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`

## Approach
1. Count the number of 0s and 1s in the array in a single pass.
2. In a second pass, overwrite the array: fill the first `r` indices with `0`, the next `w` indices with `1`, and the rest with `2`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — two passes over the array.
- **Space Complexity:** `O(1)` — only two counters used.
