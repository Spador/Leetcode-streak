# spador

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]

        lenLIS, totalCount = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            maxLen, count = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    curLen, curCount = dp[j][0], dp[j][1]
                    if curLen + 1 > maxLen:
                        maxLen = curLen + 1
                        count = curCount
                    elif curLen + 1 == maxLen:
                        count += curCount

            if maxLen > lenLIS:
                lenLIS = maxLen
                totalCount = count
            elif maxLen == lenLIS:
                totalCount += count
            dp[i][0], dp[i][1] = maxLen, count

        return totalCount
