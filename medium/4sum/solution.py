# spador

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result, curr = [], []

        # right now this is 4-sum but this solution can work for k sum
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    curr.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    curr.pop()
                return

            # base case
            left, right = start, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append(curr + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        kSum(4, 0, target)
        return result
