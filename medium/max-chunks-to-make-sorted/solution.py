from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        curr_max = -1
        result = 0
        
        for i, n in enumerate(arr):
            # Update maximum value seen so far
            curr_max = max(n, curr_max)
            
            # If maximum equals current index, we can form a valid chunk
            if curr_max == i:
                result += 1
        
        return result
