from typing import List

# spador

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n^2) solution using bottom-up dp

        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


## There is a better of O(n*logn) time complexity
