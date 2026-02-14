# 1091. Shortest Path in Binary Matrix

**Difficulty:** Medium

## Problem Description
Given an `n x n` binary matrix `grid`, return the **length of the shortest clear path** in the matrix. If there is no clear path, return `-1`.

A **clear path** in a binary matrix is a path from the top-left cell `(0, 0)` to the bottom-right cell `(n - 1, n - 1)` such that:

- All the visited cells of the path are `0`.
- All the adjacent cells of the path are **8-directionally** connected (share an edge or a corner).

The **length** of a clear path is the number of **visited cells** of this path.

## Examples

### Example 1
```
Input: grid = [[0,1],[1,0]]
Output: 2
```

### Example 2
```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```

### Example 3
```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

## Constraints
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j]` is `0` or `1`

## Approach
BFS from `(0, 0)` to `(n-1, n-1)`. Enqueue `(row, col, distance)`. For each cell, if it is out of bounds or has value `1`, skip. If it is the bottom-right cell, return the distance. Otherwise, enqueue all 8 unvisited neighbors with distance `dist + 1`. Use a visited set to avoid revisiting. If the queue is exhausted, return `-1`.

## Time & Space Complexity
- **Time Complexity:** O(n²)
- **Space Complexity:** O(n²) for the queue and visited set.
