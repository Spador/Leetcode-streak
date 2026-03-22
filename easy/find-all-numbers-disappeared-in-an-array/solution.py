# spador

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # mark the index with -ve number
        for n in nums:
            idx = abs(n) - 1
            nums[idx] = -1 * (abs(nums[idx]))

        result = []
        # append all non-negative index to the result
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i + 1)

        return result
