from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        size_old = len(nums)
        size_new = len(set(nums))

        return size_old != size_new

        #Alternate solution is to add everything to a dictionary and if duplicate is there then return 'True'
        # dic = {}
        # for i in nums:
        #     if i in dic:
        #         return True
        #     else:
        #         dic[i] = 1
        # return False 