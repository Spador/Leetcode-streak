# spador
class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)
        n = n[2:]
        l = 0
        maxgap = 0
        for r in range(len(n)):
            if n[r] == '1':
                maxgap = max(maxgap, r - l)
                l = r
        
        return maxgap
