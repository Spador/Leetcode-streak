# 797. All Paths From Source to Target

**Difficulty:** Medium

## Problem Description

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: `graph[i]` is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to `graph[i][j]`).

## Examples

### Example 1:
```
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
```

### Example 2:
```
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
```

## Constraints

- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i][j] != i (i.e., there will be no self-loops).
- All the elements of graph[i] are unique.
- The input graph is guaranteed to be a DAG.

## Approach

This problem can be solved using backtracking (DFS):

1. **Backtracking**: Explore all possible paths from source to target
2. **Path Building**: Build path as we traverse the graph
3. **Target Check**: When reaching target node (n-1), add path to result
4. **DAG Property**: No cycles, so no need to track visited nodes

## Algorithm

1. Initialize result list to store all paths
2. Define backtrack function:
   - If current node is target (n-1), add current path to result
   - For each neighbor of current node:
     - Add current node to path
     - Recursively explore neighbor
     - Backtrack (path is passed by value, so no explicit removal needed)
3. Start backtracking from node 0 with empty path
4. Return all collected paths

## Implementation Details

- **Backtracking**: Use DFS to explore all paths
- **Path Tracking**: Build path incrementally during traversal
- **No Visited Set**: DAG property ensures no cycles
- **Base Case**: Add path when reaching target node

## Key Optimizations

- **Backtracking Efficiency**: Explore all paths systematically
- **DAG Property**: No need to track visited nodes
- **Path Building**: Build path as we traverse

## Time Complexity

- **Time**: O(2^n × n) in worst case
  - There can be exponentially many paths
  - Each path can have up to n nodes
- **Space**: O(n) for recursion stack and path storage

## Solution

The solution uses backtracking (DFS):
- Explores all paths from source (0) to target (n-1)
- Builds paths incrementally during traversal
- Returns all possible paths in any order
