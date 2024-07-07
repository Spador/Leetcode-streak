from typing import List

#Spador

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # unique = 0
        # pop = 0
        # head = current = nums[0]
        # final_list = []

        # for i in range(1,len(nums) - 1):
        #     head = nums[i]
        #     if head != current:
        #         final_list.append(head)
        #         unique += 1
        #         current = nums[i+1]
            
        #     elif head == current:
        #         pop += 1
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1 