# spador

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prevBit = n & 1
        n = n >> 1
        while n:
            bit = n & 1
            n = n >> 1
            if bit ^ prevBit != 1:
                return False
            prevBit = bit
        return True
