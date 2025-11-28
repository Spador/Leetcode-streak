# 518. Coin Change II

**Difficulty:** Medium

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

## Examples

### Example 1
```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

### Example 2
```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

### Example 3
```
Input: amount = 10, coins = [10]
Output: 1
```

## Constraints
- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- All the values of `coins` are unique
- `0 <= amount <= 5000`

## Approach
1. This is a variation of the coin change problem where we count the number of ways (combinations) rather than finding the minimum number of coins.
2. Use dynamic programming with space optimization (1D array instead of 2D).
3. Work backwards through coins and amounts to build up the solution.
4. For each coin, update the DP array to include all ways we can form amounts using that coin.
5. The key insight: when processing a coin, for each amount, we can either use the coin (add ways from `amount - coin`) or skip it (keep existing ways).

## Algorithm
- Initialize `dp` array of size `amount + 1` with all zeros, except `dp[amount] = 1` (base case: one way to form amount 0 when we have amount remaining).
- For each coin `c` from the end to the beginning:
  - Create a temporary copy `tempdp = dp`.
  - For each amount `a` from `amount` down to `0`:
    - If `a + coins[c] <= amount`, add `tempdp[a + coins[c]]` to `tempdp[a]` (ways to form amount `a` by using the coin).
    - Otherwise, keep `tempdp[a]` unchanged.
  - Update `dp = tempdp`.
- Return `dp[0]` (number of ways to form the full amount).

## Time & Space Complexity
- **Time Complexity:** `O(amount * coins.length)` - nested loops over coins and amounts.
- **Space Complexity:** `O(amount)` - using a 1D array instead of 2D for space optimization.
