class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helperPalindrome(left: int, right: int):
            while(left >= 0 and right < len(s) and s[left]==s[right]):
                left-=1
                right+=1

            return s[left+1:right]
        result = ""

        for i in range(len(s)):
            test = helperPalindrome(i,i)
            if len(test) > len(result): result = test
            test = helperPalindrome(i,i+1)
            if len(test) > len(result): result = test
        
        return result 