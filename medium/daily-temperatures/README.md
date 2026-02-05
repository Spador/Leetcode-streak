# 739. Daily Temperatures

**Difficulty:** Medium

## Problem Description
Given an array of integers `temperatures` representing the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`th day to get a **warmer** temperature. If there is no future day for which this is possible, keep `answer[i] == 0` instead.

## Examples

### Example 1
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

### Example 2
```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

### Example 3
```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Approach
We use a **monotonic decreasing stack** to track indices of temperatures waiting for a warmer day:

1. Initialize an array `waits` of length `n` (same as `temperatures`) filled with `0`.
2. Maintain a stack of pairs `[temp, index]` representing days for which we haven't yet found a warmer temperature.
3. Iterate through `temperatures` with index `i` and value `temp`:
   - While the stack is not empty and `temp` is greater than the temperature at the top of the stack:
     - Pop `[t, day]` from the stack.
     - Set `waits[day] = i - day` (number of days until a warmer temperature).
   - Push `[temp, i]` onto the stack.
4. Any indices remaining in the stack have no warmer future day, so their entries in `waits` remain `0`.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, since each index is pushed and popped from the stack at most once.
- **Space Complexity:** `O(n)` for the stack and the `waits` output array.
