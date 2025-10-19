# 200. Number of Islands

**Difficulty:** Medium

## Problem Description

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Examples

### Example 1:
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

### Example 2:
```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

## Approach

This problem can be solved using Depth-First Search (DFS) or Breadth-First Search (BFS):

1. **Graph Traversal**: Treat the grid as a graph where each '1' is a node connected to adjacent '1's (up, down, left, right).
2. **Island Detection**: Each connected component of '1's represents one island.
3. **DFS/BFS Strategy**: When we find a '1', we traverse the entire connected component and mark all visited cells to avoid counting them again.

## Algorithm

1. Iterate through each cell in the grid
2. When we encounter a '1' (land):
   - Increment the island count
   - Use DFS or BFS to explore the entire connected component
   - Mark visited cells (change '1' to '0' or use a visited array)
3. Continue until all cells are processed
4. Return the total island count

## Key Considerations

- **Visited Tracking**: Mark cells as visited to avoid revisiting and double-counting
- **Boundary Checking**: Ensure we don't go out of grid bounds during traversal
- **Adjacent Cells**: Check all four directions (up, down, left, right)

## Time Complexity

- **Time**: O(m × n) where m and n are the dimensions of the grid
  - We visit each cell at most once
- **Space**: O(m × n) in the worst case for the recursion stack (DFS) or queue (BFS)

## Note

This is a classic graph traversal problem that can be solved using either DFS or BFS. The solution will explore connected components of land cells and count each as a separate island.
