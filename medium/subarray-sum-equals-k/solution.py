# spador

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currSum = 0
        prefixSum = {0 : 1}     #base case

        for n in nums:
            currSum += n
            diff = currSum - k

            result += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return result

