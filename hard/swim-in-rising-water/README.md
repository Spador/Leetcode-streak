# 778. Swim in Rising Water

**Difficulty:** Hard

## Problem Description
You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at point `(i, j)`.

It starts raining, and water gradually rises over time. At time `t`, the water level is `t`, meaning any cell with elevation less than or equal to `t` is submerged or reachable.

You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the minimum time until you can reach the bottom right square `(n - 1, n - 1)` if you start at the top left square `(0, 0)`.

## Examples

### Example 1
```
Input: grid = [[0,2],[1,3]]
Output: 3
Explanation: At time 0, you are in grid location (0, 0). You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0. You cannot reach point (1, 1) until time 3. When the depth of water is 3, we can swim anywhere inside the grid.
```

### Example 2
```
Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: The final route is shown. We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
```

## Constraints
- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 50`
- `0 <= grid[i][j] < n²`
- Each value `grid[i][j]` is unique

## Approach
1. Use Dijkstra's algorithm with a min-heap to find the path from `(0, 0)` to `(n-1, n-1)` that minimizes the maximum elevation encountered.
2. The heap stores `(max_elevation_so_far, row, col)` representing the maximum height along the path to reach that cell.
3. Start from `(0, 0)` with initial elevation `grid[0][0]`.
4. For each cell popped from the heap, explore its 4-directional neighbors.
5. For each neighbor, calculate the new maximum elevation as `max(current_max, neighbor_elevation)` and push it into the heap.
6. When we reach `(n-1, n-1)`, the maximum elevation along that path is the minimum time required.

## Algorithm
- Initialize a min-heap with `(grid[0][0], 0, 0)` and a visited set.
- While the heap is not empty:
  - Pop the cell with the smallest maximum elevation.
  - If it's the destination `(n-1, n-1)`, return the maximum elevation.
  - For each 4-directional neighbor:
    - Check if it's within bounds and not visited.
    - Calculate `new_max = max(current_max, neighbor_elevation)`.
    - Push `(new_max, neighbor_row, neighbor_col)` into the heap.
    - Mark the neighbor as visited.

## Time & Space Complexity
- **Time Complexity:** `O(n² log n)` — Dijkstra's algorithm on an n×n grid with heap operations.
- **Space Complexity:** `O(n²)` for the visited set and heap.
