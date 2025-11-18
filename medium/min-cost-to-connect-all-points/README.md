# 1584. Min Cost to Connect All Points

**Difficulty:** Medium

## Problem Description
You are given an array `points` representing integer coordinates of points on a 2D plane, where `points[i] = [x_i, y_i]`.

The cost of connecting two points `[x_i, y_i]` and `[x_j, y_j]` is their Manhattan distance: `|x_i - x_j| + |y_i - y_j|`.

Return the minimum total cost to connect all points such that there is exactly one simple path between any two points (i.e., the graph forms a tree).

## Examples

### Example 1
```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: Connect the points to form a minimum spanning tree with total cost 20.
```

### Example 2
```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints
- `1 <= points.length <= 1000`
- `-10^6 <= x_i, y_i <= 10^6`
- All point pairs `(x_i, y_i)` are distinct

## Approach
1. Treat each point as a node in a complete graph where edges represent Manhattan distances between points.
2. Use Prim's algorithm to build a minimum spanning tree (MST) without constructing all edges explicitly in memory at once.
3. Maintain a min-heap of candidate edges and a set of visited nodes.
4. Start from an arbitrary node (e.g., index 0), repeatedly pick the smallest edge leading to an unvisited node, and add it to the MST.
5. Continue until all nodes are included; the accumulated cost is the answer.

## Algorithm
- Initialize an adjacency list where each node stores the cost to every other node (since constraints allow O(n^2) preprocessing).
- Push `(0, 0)` into the min-heap to start from node 0.
- While not all nodes are visited:
  - Pop the smallest edge `(cost, node)` from the heap.
  - Skip if the node is already visited; otherwise, add the cost to the result and mark it visited.
  - Push all edges from the new node to its neighbors into the heap.
- Once every node is visited, return the accumulated cost.

## Time & Space Complexity
- **Time Complexity:** `O(n^2 log n)` due to generating all pairwise edges and heap operations.
- **Space Complexity:** `O(n^2)` for the adjacency list plus `O(n)` for the heap and visited set.
