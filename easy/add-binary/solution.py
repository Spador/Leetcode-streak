# spador

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""

        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            adigit = ord(a[i]) - ord('0') if i < len(a) else 0
            bdigit = ord(b[i]) - ord('0') if i < len(b) else 0

            total = adigit + bdigit + carry
            char = str(total % 2)
            result = char + result
            carry = total // 2
        
        if carry:
            result = "1" + result
        return result
