# spador

class Solution:
    def jump(self, nums: List[int]) -> int:

        # Greedy solution for O(n) time complexity

        result = 0
        left = right = 0

        while right < len(nums) - 1:
            far = 0
            for i in range(left, right+1):
                far = max(far, i + nums[i])
            left = right + 1
            right = far
            result += 1
        return result
        


