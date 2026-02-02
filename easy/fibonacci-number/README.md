# 509. Fibonacci Number

**Difficulty:** Easy

## Problem Description
The Fibonacci numbers, commonly denoted `F(n)`, form a sequence such that each number is the sum of the two preceding ones, starting from 0 and 1:

- `F(0) = 0`, `F(1) = 1`
- `F(n) = F(n - 1) + F(n - 2)` for `n > 1`

Given `n`, calculate `F(n)`.

## Examples

### Example 1
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```

### Example 2
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```

### Example 3
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

## Approach
We use an **iterative** approach with constant space to compute the Fibonacci number.

1. Handle the base case: if `n == 1`, return `1` (since `F(1) = 1`).
2. Initialize two variables to represent the last two Fibonacci numbers:
   - `n1 = 0` (F(0))
   - `n2 = 1` (F(1))
3. For each `i` from `2` to `n`:
   - Compute `result = n1 + n2`.
   - Shift the window: `n1 = n2`, `n2 = result`.
4. After the loop, `result` holds `F(n)`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` because we iterate from `2` to `n` once.
- **Space Complexity:** `O(1)` extra space, using only a few variables.
