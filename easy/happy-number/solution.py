# spador

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquare(n)
            if  n == 1:
                return True
        return False

    def sumOfSquare(self, n):
        squares = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
        res = 0
        while n > 0:
            digit = n % 10
            res += squares[digit]
            n //= 10
        return res
