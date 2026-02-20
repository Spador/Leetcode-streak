# spador

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currMax = 0
        result = 0

        for i in nums:
            if i:
                currMax += 1
                result = max(result, currMax)
            else:
                currMax = 0
        return result
