# spador

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxCon = 0
        numZero = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numZero += 1

            while numZero > k:
                if nums[l] == 0:
                    numZero -= 1
                l += 1
            
            maxCon = max(maxCon, (r - l + 1))
        return maxCon
