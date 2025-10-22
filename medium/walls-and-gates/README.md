# 286. Walls and Gates

**Difficulty:** Medium

## Problem Description

You are given an m x n grid rooms initialized with these three possible values.

- **-1** A wall or an obstacle.
- **0** A gate.
- **INF** Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

## Examples

### Example 1:
```
Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
```

### Example 2:
```
Input: rooms = [[-1]]
Output: [[-1]]
```

## Constraints

- m == rooms.length
- n == rooms[i].length
- 1 <= m, n <= 250
- rooms[i][j] is -1, 0, or 2^31 - 1.

## Approach

This problem can be solved using Breadth-First Search (BFS) from all gates simultaneously:

1. **Multi-source BFS**: Start from all gates (value 0) at the same time.
2. **Distance Calculation**: Use BFS to calculate shortest distance to each room.
3. **Level Processing**: Process each distance level to ensure shortest paths.
4. **In-place Update**: Modify the rooms grid directly with calculated distances.

## Algorithm

1. Find all gates (value 0) and add them to the queue
2. Use BFS to process each distance level:
   - Process all rooms at current distance level
   - Update room values with current distance
   - Add adjacent valid rooms to queue for next level
   - Increment distance for next level
3. Continue until all reachable rooms are processed

## Implementation Details

- **Multi-source BFS**: Start from all gates simultaneously
- **Level Processing**: Process all rooms at each distance level
- **Boundary Checking**: Ensure coordinates are within grid bounds
- **Visited Tracking**: Prevent revisiting rooms and handle walls

## Key Optimizations

- **Level-by-level Processing**: Ensures shortest distance calculation
- **In-place Updates**: Modify the grid directly without extra space
- **Early Termination**: Stop when no more rooms can be reached

## Time Complexity

- **Time**: O(m × n) where m and n are grid dimensions
  - We visit each cell at most once
- **Space**: O(m × n) for the queue in worst case

## Solution

The solution uses multi-source BFS:
- Starts from all gates simultaneously
- Processes each distance level to ensure shortest paths
- Updates room values in-place with calculated distances
- Handles walls and boundaries appropriately
