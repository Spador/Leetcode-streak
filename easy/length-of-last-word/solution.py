# spador

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        point = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                point -= 1
            else:
                break

        for i in range(point - 1, -1, -1):
            if s[i] == " ":
                break
            result += 1
        return result
