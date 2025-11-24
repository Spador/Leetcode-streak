from typing import List

# spador

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # bottom-up iteration DP solution
        # trying to evaluate current min and max until each number in array
        
        result = max(nums)
        currMin = 1
        currMax = 1

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
                continue
            temp = n*currMax
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(temp, n*currMin, n)
            result = max(currMax, result)

        return result

        # Time complexity = O(nums)
        # space complexity = O(1)
