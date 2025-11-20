# 746. Min Cost Climbing Stairs

**Difficulty:** Easy

## Problem Description
You are given an integer array `cost` where `cost[i]` is the cost of `i`th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return the minimum cost to reach the top of the floor.

## Examples

### Example 1
```
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

### Example 2
```
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

## Constraints
- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`

## Approach
1. This problem follows a similar pattern to Fibonacci, but working backwards from the last position.
2. The minimum cost to reach the top from step `i` is `cost[i] + min(cost[i+1], cost[i+2])`.
3. Work backwards through the array, updating each position with the minimum cost to reach the top from that step.
4. Append `0` to the cost array to represent the top of the floor (no cost to be there).
5. After processing, return the minimum of starting from index 0 or index 1.

## Algorithm
- Append `0` to the `cost` array to represent the top (no additional cost).
- Iterate backwards from `len(cost) - 3` to `0`:
  - For each step `i`, update `cost[i] += min(cost[i+1], cost[i+2])` (add current cost plus minimum of next two steps).
- Return `min(cost[0], cost[1])` as we can start from either index 0 or 1.

## Time & Space Complexity
- **Time Complexity:** `O(n)` - single pass through the array backwards.
- **Space Complexity:** `O(1)` - modifying the input array in place (excluding input space).
