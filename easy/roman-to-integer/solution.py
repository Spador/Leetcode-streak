class Solution:
    def romanToInt(self, s: str) -> int:
        # Map Roman symbols to their integer values
        romanMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        
        # Process each character in the string
        for i in range(len(s)):
            # If current value is less than next value, subtract it
            # Otherwise, add it to the result
            if (i + 1 < len(s)) and romanMap[s[i]] < romanMap[s[i + 1]]:
                result -= romanMap[s[i]]
            else:
                result += romanMap[s[i]]
        
        return result