# spador

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # if n == 1: return True
        # if n == 0: return False
        # if n % 2 == 1:
        #     return False
        # while n:
        #     n = n // 2
        #     if n == 1: return True
        #     if n % 2 == 1:
        #         return False
        # return True

        return n > 0 and not(n & (n - 1))
