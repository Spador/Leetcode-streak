from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        
        for num in arr:
            # Initialize max value for current chunk
            maxVal = num
            
            # Merge chunks if current number is smaller than previous chunk's max
            while stack and num < stack[-1]:
                value = stack.pop()
                maxVal = max(maxVal, value)
            
            # Push the maximum value of the merged chunk
            stack.append(maxVal)
        
        # Return the number of chunks (size of stack)
        return len(stack)
