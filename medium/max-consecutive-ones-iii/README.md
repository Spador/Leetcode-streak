# 1004. Max Consecutive Ones III

**Difficulty:** Medium

## Problem Description
Given a binary array `nums` and an integer `k`, return the **maximum number of consecutive 1's** in the array if you can flip at most `k` `0`'s.

## Examples

### Example 1
```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

### Example 2
```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
```

## Constraints
- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

## Approach
Use a **sliding window** with two pointers (`l` and `r`) and a counter for how many zeros are in the current window:

1. Expand the right pointer `r` over `nums`. When you see a `0`, increment the zero counter.
2. While the number of zeros in the window exceeds `k`, shrink from the left (`l`), and if you drop a `0`, decrement the zero counter.
3. At each step, the window `[l, r]` contains at most `k` zeros, so its length is a valid answer; track the maximum window size.

This effectively finds the longest subarray where you would need to flip at most `k` zeros to make all `1`s.

## Time & Space Complexity
- **Time Complexity:** O(n) — each index enters and leaves the window at most once.
- **Space Complexity:** O(1) auxiliary.
