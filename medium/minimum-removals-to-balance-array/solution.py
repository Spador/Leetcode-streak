# spador

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = n
        nums.sort()
        right = 0
        for left in range(n):
            mval = nums[left] * k
            while right < n and nums[right] <= mval:
                right += 1
            result = min(result, n - (right - left))
        return result
