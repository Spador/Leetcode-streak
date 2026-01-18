# 1752. Check if Array Is Sorted and Rotated

**Difficulty:** Easy

## Problem Description
Given an array `nums`, return `true` if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return `false`.

There may be duplicates in the original array.

Note: An array `A` rotated by `x` positions results in an array `B` of the same length such that  
`B[i] == A[(i + x) % A.length]` for every valid index `i`.

## Examples

### Example 1
```
Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 2 positions to begin on the element of value 3: [3,4,5,1,2].
```

### Example 2
```
Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
```

### Example 3
```
Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
```

## Constraints
- `1 <= nums.length <= 100`
- `1 <= nums[i] <= 100`

## Approach
For an array that is sorted in non-decreasing order and then rotated, when we scan it circularly we can see **at most one drop** where `nums[i] > nums[i+1]` (with indices taken modulo `n`).

Algorithm:
1. Let `n = len(nums)`.
2. Initialize `count = 0`.
3. For each index `i` from `0` to `n - 1`:
   - Compare `nums[i]` with `nums[(i + 1) % n]`.
   - If `nums[i] > nums[(i + 1) % n]`, increment `count`.
   - If `count > 1`, return `False` (more than one “rotation break” means it cannot be a single sorted-and-rotated array).
4. If the loop finishes with `count <= 1`, return `True`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n = len(nums)`; we scan the array once.
- **Space Complexity:** `O(1)` extra space.

