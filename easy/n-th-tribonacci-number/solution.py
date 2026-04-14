# spador

class Solution:
    def tribonacci(self, n: int) -> int:
        if n in [0, 1, 2]:
            return 0 if not n else 1

        t0, t1, t2 = 0, 1, 1

        for n in range(n - 2):
            t2, t1, t0 = (t2 + t1 + t0), t2, t1

        return t2
