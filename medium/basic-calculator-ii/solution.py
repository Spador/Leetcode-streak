import math
from typing import List

class Solution:
    def calculate(self, s: str) -> int:
        num, PreSign, stack = 0, '+', []

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) -1:
                if PreSign == '+':
                    stack.append(num)
                elif PreSign == '-':
                    stack.append(-num)
                elif PreSign == '*':
                    stack.append(stack.pop()*num)
                elif PreSign == '/':
                    stack.append(math.trunc(stack.pop()/num))
                PreSign = s[i]
                num = 0
        return sum(stack) 