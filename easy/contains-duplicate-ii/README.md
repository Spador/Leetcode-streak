# 219. Contains Duplicate II

**Difficulty:** Easy

## Problem Description
Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that:

- `nums[i] == nums[j]` and
- `abs(i - j) <= k`.

Otherwise, return `false`.

## Examples

### Example 1
```
Input: nums = [1,2,3,1], k = 3
Output: true
```

### Example 2
```
Input: nums = [1,0,1,1], k = 1
Output: true
```

### Example 3
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `0 <= k <= 10^5`

## Approach
We maintain a sliding window of at most size `k` using a set:

1. Initialize a left pointer `l = 0` and an empty set `window`.
2. Iterate `r` from `0` to `len(nums) - 1`:
   - If `r - l > k`, shrink the window from the left by removing `nums[l]` from `window` and incrementing `l`.
   - If `nums[r]` is already in `window`, we have found two equal values within distance `k`, so return `true`.
   - Otherwise, add `nums[r]` to `window`.
3. If we finish the loop without finding such a pair, return `false`.

This ensures that `window` always contains at most the last `k` elements, so any duplicate found must be at most `k` apart.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(nums)`, since each element is added and removed from the set at most once.
- **Space Complexity:** `O(k)` for the `window` set.
