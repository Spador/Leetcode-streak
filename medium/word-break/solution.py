from typing import List

# spador

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom-up iterative DP solution

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) < len(dp) and s[i:i+len(word)] == word and dp[i+ len(word)]:
                    dp[i] = True
                    break
        return dp[0]
# length of string = n and number of words = m
# Time : O(n * m * n)
# Space : O(n)
