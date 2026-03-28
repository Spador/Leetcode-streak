# spador

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float("inf")

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                elif abs(target - total) < abs(target - result):
                    result = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return result
