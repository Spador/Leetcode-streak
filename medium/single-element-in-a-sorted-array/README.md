# 540. Single Element in a Sorted Array

**Difficulty:** Medium

## Problem Description
Given a sorted array where every element appears exactly twice except for one, return the single element. Must run in `O(log n)` time and `O(1)` space.

## Examples

### Example 1
```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```

### Example 2
```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^5`

## Approach
Binary search on index parity:
1. If `mid` matches neither neighbour, it's the single element — return it.
2. Determine the left boundary of `mid`'s pair: `lefthalf = mid - 1` if paired with left, else `mid`.
3. If `lefthalf` is odd, the single element is in the left half; otherwise it's in the right half.

## Time & Space Complexity
- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`
