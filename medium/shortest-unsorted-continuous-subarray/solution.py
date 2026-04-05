# spador

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        MAX = float("-inf")
        MIN = float("inf")
        left, right = 0, 0
        # set the right pointer
        for i in range(n):
            if nums[i] >= MAX:
                MAX = nums[i]
            else:
                right = i
        # set the left limit
        for i in range(n - 1, -1, -1):
            if nums[i] <= MIN:
                MIN = nums[i]
            else:
                left = i

        return right - left + 1 if left != 0 or right != 0 else 0
