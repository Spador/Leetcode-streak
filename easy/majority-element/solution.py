# spador

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = 0, 0

        for n in nums:
            if count == 0:
                result = n
            count += 1 if n == result else -1
            # this is to make the solution faster
            if count > (len(nums)//2):
                return result

        return result
