from typing import List

# spador

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2 
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            tempdp = set()
            for n in dp:
                if (nums[i] + n) == target:
                    return True
                tempdp.add(nums[i] + n)
                tempdp.add(n)
            dp = tempdp

        return False
