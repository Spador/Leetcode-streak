# spador

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binSearch(nums, target, True)
        last = self.binSearch(nums, target, False)
        return[start, last]
        
    # leftFlag: True = finding first occurance, False = finding last occurance    
    def binSearch(self, nums, target, leftFlag):
        left, right = 0, len(nums) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                pos = mid
                if leftFlag:
                    right = mid - 1
                else:
                    left = mid + 1
        return pos

