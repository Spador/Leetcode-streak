class Solution:
    ROMAN = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def romanToInt(self, s: str) -> int:
        val = 0
        prev = 0
        
        for c in s:
            curr = self.ROMAN[c]
            if prev < curr:
                val -= prev + prev
            val += curr
            prev = curr
            
        return val 