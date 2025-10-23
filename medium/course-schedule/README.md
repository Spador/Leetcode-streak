# 207. Course Schedule

**Difficulty:** Medium

## Problem Description

There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course 0 you have to first take course 1.

Return `true` if you can finish all courses. Otherwise, return `false`.

## Examples

### Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
```

### Example 2:
```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
```

## Constraints

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

## Approach

This problem can be solved using Depth-First Search (DFS) to detect cycles in a directed graph:

1. **Graph Representation**: Build an adjacency list where each course points to its prerequisites
2. **Cycle Detection**: Use DFS with three states (unvisited, visiting, visited) to detect cycles
3. **Topological Sort**: If no cycles exist, all courses can be completed

## Algorithm

1. Build adjacency list from prerequisites
2. Use DFS with three states:
   - **Unvisited (0)**: Course not yet processed
   - **Visiting (1)**: Course currently being processed (in recursion stack)
   - **Visited (2)**: Course completely processed
3. If we encounter a course that's currently being visited, we have a cycle
4. Return true if no cycles are found

## Implementation Details

- **Graph Construction**: Create adjacency list mapping courses to their prerequisites
- **DFS with States**: Track three states to detect back edges (cycles)
- **Cycle Detection**: If we visit a node that's currently in the recursion stack, there's a cycle
- **Optimization**: Mark courses as completed to avoid redundant processing

## Key Optimizations

- **State Tracking**: Use three states to efficiently detect cycles
- **Memoization**: Mark completed courses to avoid reprocessing
- **Early Termination**: Return false immediately when cycle is detected

## Time Complexity

- **Time**: O(V + E) where V is number of courses and E is number of prerequisites
  - We visit each course and each prerequisite exactly once
- **Space**: O(V + E) for the adjacency list and recursion stack

## Solution

The solution uses DFS with cycle detection:
- Builds graph from prerequisites
- Uses three-state DFS to detect cycles
- Returns true if no cycles exist (all courses can be completed)
