from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if (numbers[l] + numbers[r]) == target:
                return [l+1, r+1]
            elif (numbers[l] + numbers[r]) < target:
                l += 1
            else:
                r -= 1
        
        return []

    def binary_search(self, numbers: List[int], goal: int) -> int:
        l, r = 0, len(numbers) - 1

        while l <= r:
            mid = (l + r) // 2
            if goal == numbers[mid]:
                return mid
            elif goal < numbers[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1 