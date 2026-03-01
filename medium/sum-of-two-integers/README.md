# 371. Sum of Two Integers

**Difficulty:** Medium

## Problem Description
Given two integers `a` and `b`, return their sum without using `+` or `-`.

## Examples

### Example 1
```
Input: a = 1, b = 2
Output: 3
```

### Example 2
```
Input: a = 2, b = 3
Output: 5
```

## Constraints
- `-1000 <= a, b <= 1000`

## Approach
Bit manipulation — simulate binary addition:
1. XOR gives the sum without carry (`a ^ b`).
2. AND then left-shift gives the carry (`(a & b) << 1`).
3. Repeat until carry is 0.

## Time & Space Complexity
- **Time Complexity:** `O(1)` — bounded by 32-bit integer width
- **Space Complexity:** `O(1)`
