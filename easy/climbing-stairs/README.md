# 70. Climbing Stairs

**Difficulty:** Easy

## Problem Description
You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## Examples

### Example 1
```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

### Example 2
```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Constraints
- `1 <= n <= 45`

## Approach
1. This problem follows a Fibonacci sequence pattern.
2. The number of ways to reach step `n` equals the sum of ways to reach step `n-1` and step `n-2`.
3. Use an iterative approach with two variables to track the previous two values, avoiding the need for a full array.
4. For small values (n < 4), return n directly as the base cases.
5. For larger values, iterate from step 3 to n, updating the two variables to compute the Fibonacci sequence.

## Algorithm
- If `n < 4`, return `n` directly (base cases: 1 step = 1 way, 2 steps = 2 ways, 3 steps = 3 ways).
- Initialize `n1 = 2` (ways to reach step 2) and `n2 = 3` (ways to reach step 3).
- For `i` in range `[0, n-3]`:
  - Update `n1, n2 = n2, n1 + n2` (shift and compute next Fibonacci number).
- Return `n2` as the number of ways to reach step `n`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` - single loop from 3 to n.
- **Space Complexity:** `O(1)` - only using two variables regardless of input size.
