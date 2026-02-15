# 231. Power of Two

**Difficulty:** Easy

## Problem Description
Given an integer `n`, return `true` if it is a power of two. Otherwise, return `false`.

An integer `n` is a power of two if there exists an integer `x` such that `n == 2^x`.

## Examples

### Example 1
```
Input: n = 1
Output: true
Explanation: 2^0 = 1
```

### Example 2
```
Input: n = 16
Output: true
Explanation: 2^4 = 16
```

### Example 3
```
Input: n = 3
Output: false
```

## Constraints
- `-2^31 <= n <= 2^31 - 1`

## Follow-up
Could you solve it without loops/recursion?

## Approach
Use a bit trick: a positive integer is a power of two **iff** it has exactly one bit set in its binary representation. For such `n`, the expression `n & (n - 1)` clears the lowest set bit and becomes `0`; for any other positive integer it stays non-zero.

So we check:
- `n > 0` to rule out non-positive numbers.
- `n & (n - 1) == 0` to ensure only one bit is set.

## Time & Space Complexity
- **Time Complexity:** O(1)
- **Space Complexity:** O(1)
