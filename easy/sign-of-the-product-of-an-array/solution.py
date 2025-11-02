from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 0  # Count of negative numbers
        
        for num in nums:
            # If any number is zero, product is zero
            if num == 0:
                return 0
            
            # Count negative numbers
            if num < 0:
                x += 1
            # Positive numbers don't affect the sign
        
        # If even number of negatives, product is positive
        # If odd number of negatives, product is negative
        if x % 2 == 0:
            return 1
        else:
            return -1
