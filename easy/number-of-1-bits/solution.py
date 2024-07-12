class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        #Solution 1: shift right and mod by 2. If remainder is 1, increment the result otherwise continue. Do this until all 32 bits are 0.

        while n:
            result += n%2
            n = n >> 1
        return result 