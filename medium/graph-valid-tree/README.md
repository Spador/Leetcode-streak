# 261. Graph Valid Tree

**Difficulty:** Medium

## Problem Description

You have a graph of n nodes labeled from 0 to n - 1. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.

## Examples

### Example 1:
```
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

### Example 2:
```
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

## Constraints

- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges.

## Approach

A valid tree must satisfy two conditions:
1. **Connected**: All nodes must be reachable from each other
2. **Acyclic**: No cycles should exist in the graph

This problem can be solved using the Union-Find algorithm:

1. **Union-Find Structure**: Use parent array and rank array for efficient union operations
2. **Cycle Detection**: If adding an edge connects already connected nodes, it creates a cycle
3. **Component Counting**: Track the number of components as we process edges
4. **Tree Validation**: A valid tree has exactly n-1 edges and is connected (1 component)

## Algorithm

1. Initialize parent array where each node is its own parent
2. Initialize rank array for union by rank optimization
3. For each edge [a, b]:
   - Find root of a and root of b
   - If roots are the same, edge creates a cycle (return false)
   - If roots are different, union the components and decrement component count
4. Check if final component count is 1 (connected graph)

## Implementation Details

- **Path Compression**: Optimize find operation by flattening the tree structure
- **Union by Rank**: Optimize union operation by attaching smaller tree to larger tree
- **Cycle Detection**: If find(a) == find(b), adding edge [a, b] creates a cycle
- **Component Tracking**: Start with n components, decrement when merging

## Key Optimizations

- **Path Compression**: Flatten tree structure during find operations
- **Union by Rank**: Balance tree heights for better performance
- **Early Termination**: Return false immediately when cycle is detected

## Time Complexity

- **Time**: O(E × α(V)) where E is number of edges and α is inverse Ackermann function
  - With path compression and union by rank, operations are nearly O(1)
- **Space**: O(V) for parent and rank arrays

## Solution

The solution uses Union-Find algorithm:
- Detects cycles by checking if nodes are already connected
- Tracks component count to ensure connectivity
- Returns true only if graph is connected and acyclic
