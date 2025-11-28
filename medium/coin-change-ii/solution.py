from typing import List

# spador
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # # bottom-up 2d dp solution
        # dp = [[0 for i in range(amount+1)] for j in range(len(coins))]
        
        # # to make amount 0, we have 1 choice to complete the amount for each coin
        # for i in range(len(coins)):
        #     dp[i][amount] = 1
        
        # for c in range(len(coins) - 1, -1, -1):
        #     for a in range(amount - 1, -1, -1):
        #         right, down = 0, 0
        #         right = dp[c][a+coins[c]] if (a + coins[c]) < amount + 1 else 0
        #         down = dp[c+1][a] if (c + 1) < len(coins) else 0
        #         dp[c][a] = down + right
        # return dp[0][0]

        # bottom-up 1d dp solution
        dp = [0 for i in range(amount + 1)]
        dp[amount] = 1

        for c in range(len(coins) - 1, -1, -1):
            tempdp = dp
            for a in range(amount, -1, -1):
                tempdp[a] = tempdp[a] + tempdp[a + coins[c]] if (a + coins[c]) < amount + 1 else tempdp[a]
            dp = tempdp
        return dp[0]
