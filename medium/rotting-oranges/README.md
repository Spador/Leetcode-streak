# 994. Rotting Oranges

**Difficulty:** Medium

## Problem Description

You are given an m x n grid where each cell can have one of three values:

- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Examples

### Example 1:
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

### Example 2:
```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
```

### Example 3:
```
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.

## Approach

This problem can be solved using Breadth-First Search (BFS) to simulate the rotting process:

1. **Multi-source BFS**: Start from all rotten oranges simultaneously.
2. **Time Simulation**: Process each level (minute) of rotting.
3. **Fresh Orange Tracking**: Count remaining fresh oranges.
4. **Impossibility Check**: Return -1 if fresh oranges remain after all possible rotting.

## Note

This is a graph traversal problem that simulates a spreading process. The solution will be implemented using BFS with level-by-level processing to track time.
