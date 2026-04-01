# spador

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        s, r = len(start), len(result)
        i, j = 0, 0
        
        
        while i < s or j < r:
            while i < s and start[i] == "X":
                i += 1
            while j < r and result[j] == "X":
                j += 1
            
            if i == s and j == r:
                return True
            if i == s or j == r:
                return False
            
            if start[i] != result[j]:
                return False
            if start[i] == "L" and i < j:
                return False
            if start[i] == "R" and i > j:
                return False
            i += 1
            j += 1
        
        return True
