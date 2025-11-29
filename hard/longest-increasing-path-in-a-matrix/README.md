# 329. Longest Increasing Path in a Matrix

**Difficulty:** Hard

## Problem Description
Given an `m x n` integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

## Examples

### Example 1
```
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
```

### Example 2
```
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

### Example 3
```
Input: matrix = [[1]]
Output: 1
```

## Constraints
- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`

## Approach
1. Use dynamic programming with memoization (DFS + caching) to avoid recomputing paths.
2. For each cell `(r, c)`, compute the longest increasing path starting from that cell.
3. Use a dictionary `dp` where `dp[(r, c)]` stores the longest increasing path length starting from cell `(r, c)`.
4. For each cell, explore all four directions (up, down, left, right) and recursively compute the path length.
5. Only move to adjacent cells if their value is greater than the current cell's value (ensuring an increasing path).
6. Cache results to avoid redundant calculations.

## Algorithm
- Initialize an empty dictionary `dp` to cache results.
- For each cell `(i, j)` in the matrix:
  - Call `dfs(i, j, -1)` to compute the longest increasing path starting from `(i, j)`.
  - The `prev` parameter ensures we only move to cells with values greater than the previous cell.
- In the `dfs` function:
  - Base cases:
    - If out of bounds or current cell value is not greater than `prev`, return `0`.
    - If `(r, c)` is already in `dp`, return the cached value.
  - Initialize `result = 1` (the current cell itself).
  - Recursively explore all four directions and take the maximum path length.
  - Cache and return the result.
- Return the maximum value in `dp`.

## Time & Space Complexity
- **Time Complexity:** `O(m * n)` where `m` and `n` are the dimensions of the matrix. Each cell is visited once and its result is cached.
- **Space Complexity:** `O(m * n)` for the `dp` dictionary and the recursion stack in the worst case.
