# 27. Remove Element

**Difficulty:** Easy

## Problem Description
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` in-place. The order of the elements may be changed. Return the number of elements `k` in `nums` which are not equal to `val`, with the first `k` elements of `nums` containing those values.

## Examples

### Example 1
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
```

### Example 2
```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
```

## Constraints
- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## Approach
Two-pointer technique:
1. Use a `left` pointer to track the position for the next valid element.
2. Iterate with `right` over all elements.
3. When `nums[right] != val`, swap it into the `left` position and advance `left`.
4. Return `left` as the count of valid elements.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — single pass through the array.
- **Space Complexity:** `O(1)` — in-place swaps, no extra space used.
