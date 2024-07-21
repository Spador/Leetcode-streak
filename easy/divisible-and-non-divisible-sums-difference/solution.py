#spador
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        numbers = [i for i in range(1, n+1)]
        num1, num2 = 0, 0

        for i in numbers:
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        
        return (num1 - num2)
