# 74. Search a 2D Matrix

**Difficulty:** Medium

## Problem Description
Given an `m x n` matrix where each row is sorted and the first integer of each row is greater than the last of the previous row, return `true` if `target` exists in the matrix. Must run in `O(log(m * n))`.

## Examples

### Example 1
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```

### Example 2
```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```

## Constraints
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## Approach
Double binary search:
1. Binary search on rows — find the row where `target` could exist (between first and last element of that row).
2. Binary search within that row for the target.

## Time & Space Complexity
- **Time Complexity:** `O(log m + log n)` = `O(log(m * n))`
- **Space Complexity:** `O(1)`
