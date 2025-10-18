class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def backtrack(index):
            if index >= len(s):
                result.append(partition[:])
                return
            
            for j in range(index, len(s)):
                if self.isPalindrome(s, index, j):
                    partition.append(s[index:j+1])
                    backtrack(j+1)
                    partition.pop()
            
        backtrack(0)
        return result
    
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
