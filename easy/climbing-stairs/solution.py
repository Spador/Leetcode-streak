# spador

# it follows a fibonacci sequence.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        n1 = 2
        n2 = 3
        for i in range(n - 3):
            n1, n2 = n2, n1 + n2
        return n2
