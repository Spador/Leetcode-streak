# 191. Number of 1 Bits

**Difficulty:** Easy

## Problem Description
Given a positive integer `n`, return the number of set bits (1s) in its binary representation (Hamming weight).

## Examples

### Example 1
```
Input: n = 11
Output: 3
```

### Example 2
```
Input: n = 128
Output: 1
```

### Example 3
```
Input: n = 2147483645
Output: 30
```

## Constraints
- `1 <= n <= 2^31 - 1`

## Approach

### Solution 1 — Shift right
Right-shift `n` one bit at a time; add `n % 2` to count each set bit until `n` is 0.

### Solution 2 — Brian Kernighan's trick
`n & (n - 1)` clears the lowest set bit. Count how many times this can be done until `n` is 0 — faster when set bits are sparse.

## Time & Space Complexity
- **Time Complexity:** `O(log n)` (Solution 1) / `O(number of set bits)` (Solution 2)
- **Space Complexity:** `O(1)`
