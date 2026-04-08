# spador

# even places can be filled in 5 ways (0, 2, 4, 6, 8)
# odd places can be filled in 4 ways (2, 3, 5, 7)

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n == 1: return 5
        mod = 10 ** 9 + 7

        def power(x, n):
            result = 1
            while n > 1:
                if n % 2:
                    result = (result * x) % mod
                x = (x * x) % mod
                n = n // 2
            return result * x

        even = ((n//2) + 1) if n % 2 else n//2
        odd = n // 2

        return (power(5, even) * power(4, odd)) % mod
