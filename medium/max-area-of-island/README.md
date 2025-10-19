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

## Algorithm

1. Iterate through each cell in the grid
2. When we encounter a '1' (land) that hasn't been visited:
   - Use DFS to explore the entire connected component
   - Count the number of cells in the island
   - Update the maximum area found
3. Return the maximum area

## Implementation Details

- **DFS Function**: Recursively explores all 4-directional neighbors
- **Boundary Checking**: Ensure coordinates are within grid bounds
- **Visited Set**: Track visited cells to avoid revisiting
- **Area Calculation**: Return 1 + sum of all connected cell areas

## Key Optimizations

- **Early Termination**: Skip cells that are water (0) or already visited
- **Set-based Visited Tracking**: O(1) lookup time for visited cells
- **Efficient DFS**: Each cell is visited exactly once

## Time Complexity

- **Time**: O(m × n) where m and n are the dimensions of the grid
  - We visit each cell at most once
- **Space**: O(m × n) in the worst case for the visited set and recursion stack

## Solution

The solution uses DFS to explore each island:
- Iterates through each cell in the grid
- When finding unvisited land ('1'), performs DFS to calculate island area
- Uses a set to avoid revisiting cells and double-counting
- Returns the maximum area found among all islands
