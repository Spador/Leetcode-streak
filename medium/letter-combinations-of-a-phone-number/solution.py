class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return
        digitCharMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def backTrack(index, currStr):
            if index >= len(digits):
                result.append(currStr)
                return
            
            for c in digitCharMap[digits[index]]:
                backTrack(index + 1, currStr + c)
        
        backTrack(0, "")
        return result
