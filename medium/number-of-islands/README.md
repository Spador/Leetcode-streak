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
3. **BFS Strategy**: When we find a '1', we use BFS to traverse the entire connected component and mark all visited cells.

## Algorithm

1. Iterate through each cell in the grid
2. When we encounter a '1' (land) that hasn't been visited:
   - Increment the island count
   - Use BFS to explore the entire connected component
   - Mark all visited cells using a set to avoid revisiting
3. Continue until all cells are processed
4. Return the total island count

## Implementation Details

- **Visited Tracking**: Use a set to track visited coordinates (row, col)
- **BFS Queue**: Use `collections.deque()` for efficient queue operations
- **Direction Array**: Check all four directions: [(0,1), (0,-1), (1,0), (-1,0)]
- **Boundary Checking**: Ensure coordinates are within grid bounds
- **DFS Alternative**: Change `q.popleft()` to `q.pop()` to convert BFS to DFS

## Key Optimizations

- **Early Return**: Return 0 immediately if grid is empty
- **Set-based Visited Tracking**: O(1) lookup time for visited cells
- **Efficient Queue Operations**: Using deque for O(1) append/pop operations

## Time Complexity

- **Time**: O(m × n) where m and n are the dimensions of the grid
  - We visit each cell at most once
- **Space**: O(m × n) in the worst case for the visited set and BFS queue

## Solution

The solution uses BFS with a visited set to track explored cells:
- Iterates through each cell in the grid
- When finding unvisited land ('1'), performs BFS to explore the entire island
- Uses a set to avoid revisiting cells and double-counting islands
- Returns the total number of distinct islands found
