# 1502. Can Make Arithmetic Progression From Sequence

**Difficulty:** Easy

## Problem Description
Given an array `arr`, return `true` if it can be rearranged to form an arithmetic progression (equal difference between all consecutive elements).

## Examples

### Example 1
```
Input: arr = [3,5,1]
Output: true
```

### Example 2
```
Input: arr = [1,2,4]
Output: false
```

## Constraints
- `2 <= arr.length <= 1000`
- `-10^6 <= arr[i] <= 10^6`

## Approach
1. Sort the array.
2. Compute the difference between the first two elements.
3. Verify all consecutive pairs have the same difference.

## Time & Space Complexity
- **Time Complexity:** `O(n log n)` — sorting dominates.
- **Space Complexity:** `O(1)`
