import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        # Build cumulative sum array
        self.cummSum = [w[0]]
        
        for i in range(len(w) - 1):
            self.cummSum.append(self.cummSum[i] + w[i + 1])
    
    def pickIndex(self) -> int:
        # Generate random target in range [0, total_sum)
        target = random.uniform(0, self.cummSum[-1])
        
        # Binary search to find the index
        l = 0
        r = len(self.cummSum)
        
        while l < r:
            mid = (l + r) // 2
            if self.cummSum[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        return l
