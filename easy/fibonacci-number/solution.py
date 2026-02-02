class Solution:
    def fib(self, n: int) -> int:
        if n == 1: return 1
        n1 = 0
        n2 = 1
        
        result = 0
        for i in range(2, n + 1):
            result = n1 + n2
            n1 = n2
            n2 = result
        return result
