# spador

# Brute Force Solution (Only works for the smaller values of n)
# Time: O(2^n)
# Space: O(2^n)
class Solution:
    def reverse(self, s: str) -> str:
        return s[::-1]

    def invert(self, s: str) -> str:
        inv = ""
        for i in range(len(s)):
            if s[i] == "1":
                inv += "0"
            else:
                inv += "1"
        return inv

    def findKthBit(self, n: int, k: int) -> str:
        S = {1 : "0"}
        for i in range(2, n + 1):
            S[i] = S[i - 1] + "1" + self.reverse(self.invert(S[i - 1]))
        return S[n][k - 1]

# spador

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = (1 << n ) - 1      # 2**n -1

        # iterative solution
        invert = False
        while length > 1:

            mid = length // 2

            if k <= mid:
                length = mid
            elif k > mid + 1:
                k = 1 + length - k
                length = mid
                invert = not invert
            else:
                return "1" if not invert else "0"
        return "0" if not invert else "1"


        # recursive solution
        def helper(length, k, invert):
            # base case:
            if length == 1:
                return "0" if not invert else "1"

            mid = length // 2

            if k <= mid:
                return helper(mid, k, invert)
            elif k > mid + 1:
                return helper(mid, 1 + length - k, not invert)
            else:
                return "1" if not invert else "0"

        return helper(length, k, False)
