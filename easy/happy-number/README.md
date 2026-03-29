# 202. Happy Number

**Difficulty:** Easy

## Problem Description
A number is happy if repeatedly replacing it with the sum of squares of its digits eventually reaches 1. Return `true` if `n` is happy, `false` if it cycles.

## Examples

### Example 1
```
Input: n = 19
Output: true
```

### Example 2
```
Input: n = 2
Output: false
```

## Constraints
- `1 <= n <= 2^31 - 1`

## Approach
1. Use a visited set to detect cycles.
2. Compute sum of squared digits using a precomputed lookup table for digits 0-9.
3. Return `true` if result reaches 1, `false` if a cycle is detected.

## Time & Space Complexity
- **Time Complexity:** `O(log n)` per iteration
- **Space Complexity:** `O(log n)` for the visited set
