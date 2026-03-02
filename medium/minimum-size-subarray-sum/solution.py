# spador

# sliding window

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        result = float("inf")
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                result = min(result, right - left + 1)
                currSum -= nums[left]
                left += 1

        return 0 if result == float("inf") else result
