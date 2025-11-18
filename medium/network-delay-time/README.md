# 743. Network Delay Time

**Difficulty:** Medium

## Problem Description
You are given a network of `n` nodes (labeled from `1` to `n`) and a list of travel times `times` represented as directed edges `times[i] = (uᵢ, vᵢ, wᵢ)` where:
- `uᵢ` is the source node
- `vᵢ` is the target node
- `wᵢ` is the time it takes for a signal to travel from `uᵢ` to `vᵢ`

A signal is sent from node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If it is impossible for all nodes to receive the signal, return `-1`.

## Examples

### Example 1
```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

### Example 2
```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

### Example 3
```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

## Constraints
- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= uᵢ, vᵢ <= n`
- `uᵢ != vᵢ`
- `0 <= wᵢ <= 100`
- All pairs `(uᵢ, vᵢ)` are unique (no multiple edges)

## Approach
1. Build an adjacency list from the `times` array to store outgoing edges and travel times for each node.
2. Run Dijkstra's algorithm using a min-heap (priority queue) starting from node `k` to propagate the signal to all nodes.
3. Keep a visited set to avoid reprocessing nodes whose shortest time has already been finalized.
4. Track the maximum time taken to reach any node; this represents the total delay once all nodes are visited.
5. If every node is reached, return the maximum time; otherwise return `-1`.

## Algorithm
- Initialize a dictionary `edges` keyed by node with a list of `(next_node, travel_time)` pairs.
- Push `(0, k)` into a min-heap representing `(current_time, node)`.
- While the heap is non-empty:
  - Pop the node with the smallest current time.
  - Skip nodes already visited to prevent redundant work.
  - Update the answer with the maximum of the current time and the running answer.
  - For each neighbor, push the accumulated time into the heap.
- After processing, return the accumulated answer if all nodes were visited; otherwise `-1`.

## Time & Space Complexity
- **Time Complexity:** `O(E log V)` — Dijkstra's algorithm with a min-heap on a sparse graph.
- **Space Complexity:** `O(E + V)` for the adjacency list, heap, and visited set.
