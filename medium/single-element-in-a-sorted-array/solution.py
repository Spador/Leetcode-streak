# spador

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)
            if ((mid - 1 < 0 or nums[mid] != nums[mid - 1]) and
                (mid + 1 == len(nums) or nums[mid] != nums[mid + 1])):
                return nums[mid]

            # check if length left half is even or odd
            # whichever half is odd, check for number in that half
            lefthalf = mid - 1 if nums[mid] == nums[mid - 1] else mid

            if lefthalf % 2:
                right = mid - 1
            else:
                left = mid + 1

        return nums[right]
