# 312. Burst Balloons

**Difficulty:** Hard

## Problem Description
You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons.

If you burst the `i`th balloon, you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of bounds of the array, then treat it as if there is a balloon with a `1` painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

## Examples

### Example 1
```
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```

### Example 2
```
Input: nums = [1,5]
Output: 10
```

## Constraints
- `n == nums.length`
- `1 <= n <= 300`
- `0 <= nums[i] <= 100`

## Approach
This is a classic interval dynamic programming problem.

The difficulty comes from the fact that bursting a balloon affects its neighbors, so the order in which we burst balloons matters. Instead of thinking about which balloon to burst **first**, we think in reverse: for any interval, choose which balloon to burst **last**.

1. Pad the original array with `1` at both ends: `nums = [1] + nums + [1]`. This makes edge handling easier when computing coins.
2. Use a top-down recursive DP with memoization on intervals.
3. Define `dfs(l, r)` as the maximum coins we can collect by bursting all balloons in the open interval `[l, r]` (inclusive) of the padded `nums` array.
4. If `l > r`, there are no balloons to burst, so return `0`.
5. For each possible last balloon `i` in the interval `[l, r]`:
   - If we pop `i` last, the coins gained are:
     - `nums[l - 1] * nums[i] * nums[r + 1]` (neighbors just outside the interval),
     - plus the best we can do in the left interval `[l, i - 1]`,
     - plus the best we can do in the right interval `[i + 1, r]`.
   - Take the maximum over all choices of `i`.
6. Memoize results in a dictionary `dp[(l, r)]` to avoid recomputation.

## Algorithm
- Pad the array: `nums = [1] + nums + [1]`.
- Initialize a dictionary `dp = {}`.
- Define a recursive function `dfs(l, r)`:
  - If `l > r`, return `0`.
  - If `(l, r)` is in `dp`, return `dp[(l, r)]`.
  - Initialize `dp[(l, r)] = 0`.
  - For each `i` from `l` to `r`:
    - `coins = nums[l - 1] * nums[i] * nums[r + 1]`
    - `coins += dfs(l, i - 1) + dfs(i + 1, r)`
    - `dp[(l, r)] = max(dp[(l, r)], coins)`
  - Return `dp[(l, r)]`.
- The answer is `dfs(1, len(nums) - 2)` (the original range without the padded `1`s).

## Time & Space Complexity
- **Time Complexity:** `O(n^3)` in the worst case, where `n` is the length of the original `nums` array. There are `O(n^2)` intervals and for each interval we try `O(n)` possible last balloons.
- **Space Complexity:** `O(n^2)` for the DP dictionary and recursion stack.

