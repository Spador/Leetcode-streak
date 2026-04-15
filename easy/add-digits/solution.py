# spador

# to check if a number is divisible by 9, we check if the sum of its digit is divisible by 9
# If we convert number recursilvely by adding all its digit and check its modulo with 9,
# then we can find the single digit number and that remainder will be the recursive sum of digits.

# Basically my thought process is that how much shorter is the number to get divisible by 9


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
