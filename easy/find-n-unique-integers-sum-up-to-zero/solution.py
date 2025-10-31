from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        if n % 2 == 1:
            # For odd n, generate symmetric integers around zero
            for i in range(-(n // 2), (n // 2) + 1, 1):
                result.append(i)
        else:
            # For even n, generate consecutive positive integers
            for i in range(1, n):
                result.append(i)
            # Add negative sum to make total sum zero
            result.append(-(n * (n - 1)) // 2)
        
        return result
