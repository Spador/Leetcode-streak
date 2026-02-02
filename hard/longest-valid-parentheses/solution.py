# spador

# Time: O(n +n) = O(n)
# Space: O(1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lcount = rcount = 0
        result = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                lcount += 1
            else:
                rcount += 1
            
            if rcount == lcount:
                result = max(result, lcount + rcount)
            elif rcount > lcount:
                lcount = rcount = 0
            i += 1
        
        lcount = rcount = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == "(":
                lcount += 1
            else:
                rcount += 1
            
            if rcount == lcount:
                result = max(result, lcount + rcount)
            elif rcount < lcount:
                lcount = rcount = 0
            i -= 1

        return result
