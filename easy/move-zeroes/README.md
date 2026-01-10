# 283. Move Zeroes

**Difficulty:** Easy

## Problem Description
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this **in-place** without making a copy of the array.

## Examples

### Example 1
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

### Example 2
```
Input: nums = [0]
Output: [0]
```

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Approach
We use a **two-pointer** technique to move all non-zero elements to the front while preserving their relative order, and implicitly push zeros to the end.

1. Maintain a pointer `left` that tracks the position where the next non-zero element should be placed.
2. Iterate with `right` from `0` to `len(nums) - 1`:
   - If `nums[right] != 0`, swap `nums[left]` and `nums[right]`, then increment `left`.
3. All non-zero elements will be compacted at the beginning of the array, in their original relative order, and all positions after `left` will contain zeros.

This approach works in-place and does not require extra memory.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n = len(nums)`, since we scan the array once.
- **Space Complexity:** `O(1)` additional space.

