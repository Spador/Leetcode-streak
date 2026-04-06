# spador

class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        result, bit = num, 1
        while num:
            result = result ^ bit
            bit <<= 1
            num >>= 1
        return result
