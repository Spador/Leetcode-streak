# 323. Number of Connected Components in an Undirected Graph

**Difficulty:** Medium

## Problem Description

You have a graph of n nodes. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return the number of connected components in the graph.

## Examples

### Example 1:
```
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

### Example 2:
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

## Constraints

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.

## Approach

This problem can be solved using the Union-Find (Disjoint Set Union) algorithm to count connected components:

1. **Union-Find Structure**: Use parent array and rank array for efficient union operations
2. **Component Counting**: Start with n components (each node is its own component)
3. **Edge Processing**: For each edge, union the two nodes if they're in different components
4. **Component Reduction**: Decrease component count when two components are merged

## Algorithm

1. Initialize parent array where each node is its own parent
2. Initialize rank array for union by rank optimization
3. Start with n components (one per node)
4. For each edge [a, b]:
   - Find root of a and root of b
   - If roots are different, union the components and decrement count
   - If roots are same, nodes are already connected (no change)
5. Return the final component count

## Implementation Details

- **Path Compression**: Optimize find operation by flattening the tree structure
- **Union by Rank**: Optimize union operation by attaching smaller tree to larger tree
- **Component Tracking**: Start with n components and decrement when merging
- **Edge Processing**: Process all edges to connect all possible components

## Key Optimizations

- **Path Compression**: Flatten tree structure during find operations
- **Union by Rank**: Balance tree heights for better performance
- **Component Counting**: Efficiently track number of remaining components

## Time Complexity

- **Time**: O(E × α(V)) where E is number of edges and α is inverse Ackermann function
  - With path compression and union by rank, operations are nearly O(1)
- **Space**: O(V) for parent and rank arrays

## Solution

The solution uses Union-Find algorithm:
- Processes all edges to connect components
- Tracks component count by decrementing when merging
- Returns the final number of connected components
