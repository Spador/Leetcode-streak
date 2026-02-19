# spador

# Algo
# pointer at end moves towards start till order is ascending
# once the condition breaks, reverse everything till that point
# then swap that point with the next number bigger than that


class Solution:
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def reverse(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        if len(nums) == 2:
            self.swap(nums, 0, 1)
            return

        rev = len(nums) - 2
        while rev >= 0 and nums[rev] >=  nums[rev + 1]:
            rev -= 1
        self.reverse(nums, rev + 1, len(nums) - 1)
        if rev == -1:
            return
        next_num = rev + 1
        while next_num < len(nums) and nums[next_num] <= nums[rev]:
            next_num += 1
        self.swap(nums, next_num, rev)
        return
