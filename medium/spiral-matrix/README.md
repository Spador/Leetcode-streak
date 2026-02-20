# 54. Spiral Matrix

**Difficulty:** Medium

## Problem Description
Given an `m x n` matrix, return all elements of the matrix in spiral order.

## Examples

### Example 1
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

### Example 2
```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints
- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Approach
Layer-by-layer traversal using four boundary pointers (`left`, `right`, `top`, `bottom`):
1. Traverse the top row left to right, then shrink `top`.
2. Traverse the right column top to bottom, then shrink `right`.
3. Check boundaries — break early if the remaining region is exhausted.
4. Traverse the bottom row right to left, then shrink `bottom`.
5. Traverse the left column bottom to top, then shrink `left`.
6. Repeat until boundaries cross.

## Time & Space Complexity
- **Time Complexity:** `O(m * n)` — every element visited once.
- **Space Complexity:** `O(1)` extra (result list excluded).
