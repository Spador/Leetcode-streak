# 210. Course Schedule II

**Difficulty:** Medium

## Problem Description

There are a total of `numCourses` courses you have to take, labeled from 0 to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

## Examples

### Example 1:
```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

### Example 2:
```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

### Example 3:
```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

## Constraints

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- ai != bi
- All the pairs [ai, bi] are distinct.

## Approach

This problem extends Course Schedule I by requiring us to return the actual ordering of courses. We can solve this using Depth-First Search (DFS) with topological sorting:

1. **Graph Representation**: Build an adjacency list where each course points to its prerequisites
2. **Cycle Detection**: Use DFS with three states to detect cycles
3. **Topological Order**: Build the result array by adding courses in post-order DFS
4. **Result Construction**: Return the topological ordering or empty array if cycle exists

## Algorithm

1. Build adjacency list from prerequisites
2. Use DFS with three states:
   - **Unvisited**: Course not yet processed
   - **Visiting**: Course currently being processed (in recursion stack)
   - **Visited**: Course completely processed
3. If we encounter a course that's currently being visited, we have a cycle
4. Add courses to result in post-order (after processing all prerequisites)
5. Return result if no cycles, otherwise empty array

## Implementation Details

- **Graph Construction**: Create adjacency list mapping courses to their prerequisites
- **DFS with States**: Track visiting and visited states to detect cycles
- **Post-order Processing**: Add courses to result after processing all prerequisites
- **Cycle Detection**: If we visit a node that's currently in the recursion stack, there's a cycle

## Key Optimizations

- **State Tracking**: Use visiting and visited sets to efficiently detect cycles
- **Post-order DFS**: Build topological order by adding courses after processing prerequisites
- **Early Termination**: Return empty array immediately when cycle is detected

## Time Complexity

- **Time**: O(V + E) where V is number of courses and E is number of prerequisites
  - We visit each course and each prerequisite exactly once
- **Space**: O(V + E) for the adjacency list and recursion stack

## Solution

The solution uses DFS with topological sorting:
- Builds graph from prerequisites
- Uses three-state DFS to detect cycles and build ordering
- Returns topological ordering if no cycles exist, otherwise empty array
