# 309. Best Time to Buy and Sell Stock with Cooldown

**Difficulty:** Medium

## Problem Description
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

## Examples

### Example 1
```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

### Example 2
```
Input: prices = [1]
Output: 0
```

## Constraints
- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`

## Approach
1. Use dynamic programming with memoization (top-down approach) to explore all possible states.
2. Track two states: `buying` (True) and `selling` (False).
3. At each day `i`:
   - **If buying (state = True)**: 
     - Option 1: Buy the stock (move to selling state, go to next day) and subtract the price.
     - Option 2: Cooldown (stay in buying state, go to next day).
   - **If selling (state = False)**:
     - Option 1: Sell the stock (move to buying state, skip one day for cooldown) and add the price.
     - Option 2: Cooldown (stay in selling state, go to next day).
4. Use memoization to cache results for `(i, state)` pairs to avoid recalculating the same subproblems.
5. Base case: if we've reached the end of the array, return 0 (no more profit possible).

## Algorithm
- Initialize a memoization dictionary `dp` with keys `(i, state)`.
- Define recursive function `dfs(i, state)`:
  - If `i >= len(prices)`, return 0.
  - If `(i, state)` is in `dp`, return cached value.
  - If `state == True` (buying):
    - `buy = dfs(i + 1, False) - prices[i]` (buy now, move to selling state).
    - `cooldown = dfs(i + 1, True)` (skip this day).
    - Store `max(buy, cooldown)` in `dp[(i, state)]`.
  - If `state == False` (selling):
    - `sell = dfs(i + 2, True) + prices[i]` (sell now, skip next day for cooldown, move to buying state).
    - `cooldown = dfs(i + 1, False)` (skip this day).
    - Store `max(sell, cooldown)` in `dp[(i, state)]`.
  - Return `dp[(i, state)]`.
- Call `dfs(0, True)` to start in buying state.

## Time & Space Complexity
- **Time Complexity:** `O(n)` - each state `(i, state)` is computed once, and there are `2n` possible states.
- **Space Complexity:** `O(n)` - for the memoization dictionary and recursion stack.
