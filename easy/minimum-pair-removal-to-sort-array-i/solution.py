# spador

class Solution:
    def isSorted(self, num: List[int]) -> bool:
        prev = num[0]
        for n in num[1:]:
            if n < prev:
                return False
            prev = n
        return True
    
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        
        while not self.isSorted(nums):
            minSum = float('inf')
            idx = 0
            
            for i in range(len(nums) - 1):
                currSum = nums[i] + nums[i+1]
                if currSum < minSum:
                    minSum = currSum
                    idx = i
            
            nums[idx] = minSum
            nums.pop(idx + 1)
            ops += 1
            
        return ops
