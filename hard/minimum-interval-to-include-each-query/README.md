# 1851. Minimum Interval to Include Each Query

**Difficulty:** Hard

## Problem Description
Given intervals and queries, for each query return the size of the smallest interval that contains it, or `-1` if none exists.

## Examples

### Example 1
```
Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
```

### Example 2
```
Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
```

## Constraints
- `1 <= intervals.length, queries.length <= 10^5`
- `1 <= lefti <= righti <= 10^7`
- `1 <= queries[j] <= 10^7`

## Approach
Sort intervals + sorted queries + min-heap:
1. Sort intervals by start. Process queries in sorted order.
2. For each query, push all intervals whose start <= query onto a min-heap keyed by size.
3. Pop intervals from the heap whose end < query (they can no longer cover this or future queries).
4. The heap top is the smallest valid interval. Store result by query value, then map back to original order.

## Time & Space Complexity
- **Time Complexity:** `O((n + q) log n)`
- **Space Complexity:** `O(n + q)`
