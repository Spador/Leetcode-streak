from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index: int) -> None:
            if index >= len(nums):
                result.append(subset.copy())
                return
            
            # decision to include nums[index]
            subset.append(nums[index])
            backtrack(index + 1)

            # decision to not include nums[index]
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result
