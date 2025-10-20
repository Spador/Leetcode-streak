# 417. Pacific Atlantic Water Flow

**Difficulty:** Medium

## Problem Description

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

## Examples

### Example 1:
```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

### Example 2:
```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

## Constraints

- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 105

## Approach

This problem can be solved using Depth-First Search (DFS) from the ocean boundaries:

1. **Reverse Flow Analysis**: Instead of checking if water can flow from each cell to oceans, we start from ocean boundaries and see which cells can be reached.
2. **Two Ocean Tracking**: Use separate sets to track cells that can reach Pacific and Atlantic oceans.
3. **Intersection**: Find cells that can reach both oceans.

## Algorithm

1. Create two sets: `pac` for Pacific-reachable cells and `atl` for Atlantic-reachable cells
2. Start DFS from Pacific boundaries (top and left edges):
   - Top row: DFS from each cell
   - Left column: DFS from each cell
3. Start DFS from Atlantic boundaries (bottom and right edges):
   - Bottom row: DFS from each cell
   - Right column: DFS from each cell
4. Find intersection of both sets to get cells that can reach both oceans

## Implementation Details

- **DFS Function**: Recursively explores all 4-directional neighbors
- **Height Constraint**: Water can only flow to cells with height <= current height
- **Boundary Checking**: Ensure coordinates are within grid bounds
- **Visited Tracking**: Use sets to track reachable cells from each ocean

## Key Optimizations

- **Reverse Flow**: Start from ocean boundaries instead of checking each cell
- **Set Operations**: Use set intersection to find cells reachable by both oceans
- **Efficient DFS**: Each cell is visited at most twice (once per ocean)

## Time Complexity

- **Time**: O(m × n) where m and n are the dimensions of the grid
  - We visit each cell at most twice (once per ocean)
- **Space**: O(m × n) for the sets and recursion stack

## Solution

The solution uses reverse DFS from ocean boundaries:
- Starts DFS from Pacific boundaries (top and left edges)
- Starts DFS from Atlantic boundaries (bottom and right edges)
- Uses set intersection to find cells reachable by both oceans
- Returns coordinates of cells that can flow to both Pacific and Atlantic oceans
