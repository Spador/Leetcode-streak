# 133. Clone Graph

**Difficulty:** Medium

## Problem Description

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

## Test Case Format

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

## Examples

### Example 1:
```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
```

### Example 2:
```
Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
```

### Example 3:
```
Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
```

## Constraints

- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

## Approach

This problem can be solved using Depth-First Search (DFS) with a hash map to track cloned nodes:

1. **Hash Map Tracking**: Use a dictionary to map original nodes to their cloned copies.
2. **DFS Traversal**: Recursively traverse the graph and clone each node.
3. **Cycle Prevention**: Check if a node has already been cloned to avoid infinite loops.
4. **Neighbor Cloning**: For each node, recursively clone all its neighbors.

## Algorithm

1. Create a hash map `oldToNew` to track cloned nodes
2. Use DFS to traverse the graph:
   - If node is already cloned, return the cloned version
   - Create a new node with the same value
   - Add the mapping to the hash map
   - Recursively clone all neighbors
   - Add cloned neighbors to the new node's neighbors list
3. Return the cloned node

## Key Optimizations

- **Memoization**: Use hash map to avoid re-cloning the same node
- **Cycle Detection**: Hash map prevents infinite recursion in cyclic graphs
- **Efficient Traversal**: DFS ensures each node is visited exactly once

## Time Complexity

- **Time**: O(V + E) where V is the number of vertices and E is the number of edges
  - We visit each node and edge exactly once
- **Space**: O(V) for the hash map and recursion stack

## Solution

The solution uses DFS with memoization:
- Maps original nodes to their cloned copies using a hash map
- Recursively clones each node and its neighbors
- Prevents infinite loops by checking if a node has already been cloned
- Returns the cloned graph starting from the given node
