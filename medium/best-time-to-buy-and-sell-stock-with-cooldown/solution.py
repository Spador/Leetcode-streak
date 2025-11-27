from typing import List

# spador

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # state: buying(True) and sell(False)
        # buy: i + 1
        # sell: i + 2
        dp = {}     # Key = (i, state), Value = max profit
        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in dp:
                return dp[(i, state)]
            
            # buying
            if state:
                buy = dfs(i + 1, not state) - prices[i]
                cooldown = dfs(i + 1, state)
                dp[(i, state)] = max(buy, cooldown)
            # sell
            else:
                sell = dfs(i + 2, not state) + prices[i]
                cooldown = dfs(i + 1, state)
                dp[(i, state)] = max(sell, cooldown)
            return dp[(i, state)]
        return dfs(0, True)
