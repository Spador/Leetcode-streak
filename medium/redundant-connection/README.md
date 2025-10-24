# 684. Redundant Connection

**Difficulty:** Medium

## Problem Description

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array `edges` of length n where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

## Examples

### Example 1:
```
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
```

### Example 2:
```
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
```

## Constraints

- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.

## Approach

This problem can be solved using the Union-Find (Disjoint Set Union) algorithm to detect the redundant edge:

1. **Union-Find Structure**: Use parent array and rank array for efficient union operations
2. **Edge Processing**: Process edges in order and attempt to union their endpoints
3. **Cycle Detection**: If two nodes are already connected, adding the edge creates a cycle
4. **Result**: Return the first edge that creates a cycle (which is the redundant edge)

## Algorithm

1. Initialize parent array where each node is its own parent
2. Initialize rank array for union by rank optimization
3. For each edge [a, b]:
   - Find root of a and root of b
   - If roots are the same, edge [a, b] creates a cycle (redundant)
   - If roots are different, union the two components
4. Return the edge that creates the cycle

## Implementation Details

- **Path Compression**: Optimize find operation by flattening the tree structure
- **Union by Rank**: Optimize union operation by attaching smaller tree to larger tree
- **Cycle Detection**: If find(a) == find(b), adding edge [a, b] creates a cycle
- **Edge Order**: Process edges in given order to return the last redundant edge

## Key Optimizations

- **Path Compression**: Flatten tree structure during find operations
- **Union by Rank**: Balance tree heights for better performance
- **Early Termination**: Return immediately when cycle is detected

## Time Complexity

- **Time**: O(E × α(V)) where E is number of edges and α is inverse Ackermann function
  - With path compression and union by rank, operations are nearly O(1)
- **Space**: O(V) for parent and rank arrays

## Solution

The solution uses Union-Find algorithm:
- Processes edges in order
- Detects cycle when adding an edge connects already connected components
- Returns the redundant edge that creates the cycle
