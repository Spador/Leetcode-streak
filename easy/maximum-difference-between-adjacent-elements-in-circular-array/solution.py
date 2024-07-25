##spador

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDiff = abs(nums[-1] - nums[0])
        i = 0
        while i < len(nums)-1:
            maxDiff = max(maxDiff, abs(nums[i]-nums[i+1]))
            i += 1
        return maxDiff
