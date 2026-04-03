# spador

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle: return 0

        left = 0

        for right in range(len(needle), len(haystack) + 1):
            if haystack[left:right] == needle:
                return left
            left += 1
        return -1
