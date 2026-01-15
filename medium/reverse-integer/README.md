# 7. Reverse Integer

**Difficulty:** Medium

## Problem Description
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-2^31, 2^31 - 1]`, then return `0`.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Examples

### Example 1
```
Input: x = 123
Output: 321
```

### Example 2
```
Input: x = -123
Output: -321
```

### Example 3
```
Input: x = 120
Output: 21
```

## Constraints
- `-2^31 <= x <= 2^31 - 1`

## Approach
We reverse the integer digit by digit using arithmetic (no string conversion), and carefully check for 32-bit overflow on each step.

Steps:
1. Define constants:
   - `MIN = -2^31  = -2147483648`
   - `MAX =  2^31 - 1 = 2147483647`
2. Initialize `result = 0`.
3. While `x` is not `0`:
   - Extract the last digit using `digit = int(math.fmod(x, 10))` (so it works correctly for negative numbers).
   - Remove the last digit via `x = int(x / 10)`.
   - Before updating `result = result * 10 + digit`, check for overflow:
     - If `result > MAX // 10` or (`result == MAX // 10` and `digit > MAX % 10`), then it would overflow the positive limit, so return `0`.
     - If `result < MIN // 10` or (`result == MIN // 10` and `digit < MIN % 10`), then it would overflow the negative limit, so return `0`.
   - Otherwise, update `result = result * 10 + digit`.
4. Return `result`.

This ensures we never actually store a value outside the 32-bit signed integer range.

## Time & Space Complexity
- **Time Complexity:** `O(k)`, where `k` is the number of digits in `x` (at most 10 for 32-bit integers).
- **Space Complexity:** `O(1)`, using only a few variables.

