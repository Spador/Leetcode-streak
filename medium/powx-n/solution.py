# spador

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(x, n):
            # base case 1
            if x == 0:
                return 0
            # base case 2
            if n == 0:
                return 1

            res = power(x, n // 2)
            res = res * res
            return res if not n % 2 else res * x

        result = power(x, abs(n))
        return result if n >= 0 else (1 / result)
