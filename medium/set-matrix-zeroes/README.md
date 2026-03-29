# 73. Set Matrix Zeroes

**Difficulty:** Medium

## Problem Description
Given an `m x n` matrix, if an element is `0`, set its entire row and column to `0` in-place.

## Examples

### Example 1
```
Input:  [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

### Example 2
```
Input:  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Constraints
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Approach
O(1) space using the first row and column as markers:
1. Scan the matrix; for each zero at `(r, c)`, mark `matrix[0][c] = 0` and `matrix[r][0] = 0`. Track `(0,0)` separately with an `origin` flag since it's shared.
2. Zero out inner cells `(r >= 1, c >= 1)` based on markers in row 0 / col 0.
3. Zero out col 0 if `matrix[0][0] == 0`.
4. Zero out row 0 if `origin` is set.

## Time & Space Complexity
- **Time Complexity:** `O(m * n)`
- **Space Complexity:** `O(1)`
