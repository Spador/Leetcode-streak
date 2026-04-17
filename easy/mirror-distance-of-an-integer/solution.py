# spador

class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        result = n
        while n:
            rev = (rev * 10) + (n % 10)
            n = n // 10
        return abs(result - rev)
