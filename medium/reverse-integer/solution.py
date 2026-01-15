class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648   # 32 bit negative integer
        MAX = 2147483647    # 32 bit positive integer
        result = 0
        while x:
            digit = int(math.fmod(x,10))    # To ensure correct mod in case of -ve
            x = int(x/10)

            if (result > MAX // 10) or (result == MAX // 10 and digit > MAX % 10 ):
                return 0
            if (result < MIN // 10) or (result == MIN // 10 and digit < MIN % 10 ):
                return 0
            result = result*10 + digit
        
        return result


