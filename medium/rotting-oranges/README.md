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

## Algorithm

1. Initialize queue with all rotten oranges and count fresh oranges
2. Use BFS to process each minute:
   - Process all oranges that will rot in current minute
   - Add newly rotten oranges to queue
   - Decrement fresh orange count
   - Increment time
3. Return time if no fresh oranges remain, otherwise -1

## Implementation Details

- **Multi-source BFS**: Start from all rotten oranges at once
- **Level Processing**: Process all oranges that rot in each minute
- **Fresh Tracking**: Count and decrement fresh oranges as they rot
- **Boundary Checking**: Ensure coordinates are within grid bounds

## Key Optimizations

- **Level-by-level Processing**: Process all oranges that rot in each minute
- **Fresh Orange Counter**: Track remaining fresh oranges efficiently
- **Early Termination**: Stop when no more oranges can rot

## Time Complexity

- **Time**: O(m × n) where m and n are grid dimensions
  - We visit each cell at most once
- **Space**: O(m × n) for the queue in worst case

## Solution

The solution uses multi-source BFS:
- Starts from all rotten oranges simultaneously
- Processes each minute level by level
- Tracks fresh orange count and time
- Returns minimum time or -1 if impossible
