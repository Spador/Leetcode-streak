# spador

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # There is a DP solution but Greedy solution is O(n) time and O(1) space

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False

        

