# 189. Rotate Array

**Difficulty:** Medium

## Problem Description
Given an integer array `nums`, rotate it to the right by `k` steps in-place.

## Examples

### Example 1
```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

### Example 2
```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
```

## Constraints
- `1 <= nums.length <= 10^5`
- `0 <= k <= 10^5`

## Approach
Three-reverse trick:
1. Normalize `k = k % n`.
2. Reverse the entire array.
3. Reverse first `k` elements.
4. Reverse the remaining `n - k` elements.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
