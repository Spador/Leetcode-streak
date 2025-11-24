# 322. Coin Change

**Difficulty:** Medium

## Problem Description
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

## Examples

### Example 1
```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

### Example 2
```
Input: coins = [2], amount = 3
Output: -1
```

### Example 3
```
Input: coins = [1], amount = 0
Output: 0
```

## Constraints
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Approach
1. This is a classic dynamic programming problem (unbounded knapsack variant).
2. Use bottom-up DP where `dp[i]` represents the minimum number of coins needed to make amount `i`.
3. Initialize `dp[0] = 0` (0 coins needed for amount 0) and all other values to a large number (e.g., `amount + 1`).
4. For each amount from 1 to `amount`, try each coin denomination:
   - If the coin can be used (i.e., `i - coin >= 0`), update `dp[i] = min(dp[i], 1 + dp[i - coin])`.
5. After processing, if `dp[amount]` is still the initial large value, return `-1`; otherwise return `dp[amount]`.

## Algorithm
- Initialize `dp` array of size `amount + 1` with all values set to `amount + 1` (impossible value).
- Set `dp[0] = 0` as base case (0 coins for amount 0).
- For each amount `i` from 1 to `amount`:
  - For each coin `c` in `coins`:
    - If `i - c >= 0`, update `dp[i] = min(dp[i], 1 + dp[i - c])`.
- Return `dp[amount]` if it's not `amount + 1`, otherwise return `-1`.

## Time & Space Complexity
- **Time Complexity:** `O(amount * coins.length)` - nested loops over amount and coins.
- **Space Complexity:** `O(amount)` - for the DP array.
