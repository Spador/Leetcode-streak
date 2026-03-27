# spador

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        counter = len(nums) - 1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                result[counter] =  nums[left] ** 2
                left += 1
            elif abs(nums[right]) > abs(nums[left]):
                result[counter] =  nums[right] ** 2
                right -= 1
            counter -= 1

        return result
