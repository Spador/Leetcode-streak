# 50. Pow(x, n)

**Difficulty:** Medium

## Problem Description
Implement `pow(x, n)` — x raised to the power n.

## Examples

### Example 1
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

### Example 2
```
Input: x = 2.10000, n = 3
Output: 9.26100
```

### Example 3
```
Input: x = 2.00000, n = -2
Output: 0.25000
```

## Constraints
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`

## Approach
Fast exponentiation (divide and conquer):
1. Recursively compute `power(x, n // 2)` and square it.
2. If `n` is odd, multiply by `x` once more.
3. Handle negative `n` by computing `power(x, abs(n))` then taking the reciprocal.

## Time & Space Complexity
- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(log n)` recursion stack
