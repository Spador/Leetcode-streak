# 695. Max Area of Island

**Difficulty:** Medium

## Problem Description

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

## Examples

### Example 1:
```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

### Example 2:
```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 50
- grid[i][j] is either 0 or 1.

## Approach

This problem can be solved using Depth-First Search (DFS) to explore each island and calculate its area:

1. **Island Detection**: Find all connected components of 1's in the grid.
2. **Area Calculation**: For each island, count the number of cells using DFS.
3. **Maximum Tracking**: Keep track of the largest island area found.
4. **Visited Tracking**: Mark visited cells to avoid recounting.

## Note

This is a graph traversal problem that requires exploring connected components and calculating their areas. The solution will be implemented using DFS with proper boundary checking and visited cell tracking.
