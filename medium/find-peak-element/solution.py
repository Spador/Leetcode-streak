# spador

# This is a tricky question.
# Facts: since it says to solve in O(logN) time so it gaurentees that we have 
# to use binary search. Also no adjacent elements are equal. Peak is guarenteed.
# We will try to move towards pointer which has higher value for neighbor than mid by making 
# one of the 2 assumptions:
# 1. Either it is strictly increasing, which means we will find peak at end of the array
# 2. It might dip somewhere, which means we found peak just before the dip.


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0 , len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            # if we assume left side is increasing
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1
            # if we assume right side in increasing
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                return mid
        


