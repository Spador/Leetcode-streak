# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium

## Problem Description
Given a sorted array, remove duplicates in-place so each unique element appears at most twice. Return `k` — the count of valid elements.

## Examples

### Example 1
```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
```

### Example 2
```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
```

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- Sorted in non-decreasing order.

## Approach
Two pointers: use `right` to scan groups of equal elements, count their occurrences, then copy at most 2 into the `left` position.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
