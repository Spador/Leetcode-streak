# spador

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        # finding GCD of the length of the 2 strings
        l1, l2 = len(str1), len(str2)
        while l2:
            l1, l2 = l2, l1 % l2

        return str1[:l1]
