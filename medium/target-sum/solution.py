from typing import List

# spador

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # backtracking solution with cache
        # Time: O(n * m) where n = # of number & m = range[min total, max total]
        # Space: O(n * m)
        
        dp = {}     # key: (index, total) -> # number of ways to reach sum

        def backtrack(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]
            
            dp[(index, total)] = backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index])

            return dp[(index, total)]
        return backtrack(0, 0)
