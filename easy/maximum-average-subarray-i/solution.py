# spador

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = 0
        for i in range(k):
            currSum += nums[i]

        result = currSum
        left = 0
        for right in range(k, len(nums)):
            currSum += (nums[right] - nums[left])
            result = max(result, currSum)
            left += 1
        return result / k
