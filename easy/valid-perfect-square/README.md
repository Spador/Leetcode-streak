# 367. Valid Perfect Square

**Difficulty:** Easy

## Problem Description
Given a positive integer `num`, return `true` if it is a perfect square without using any built-in library function like `sqrt`.

## Examples

### Example 1
```
Input: num = 16
Output: true
```

### Example 2
```
Input: num = 14
Output: false
```

## Constraints
- `1 <= num <= 2^31 - 1`

## Approach
Binary search between `1` and `num`. For each `mid`, check if `mid * mid == num`. Narrow left/right accordingly.

## Time & Space Complexity
- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`
