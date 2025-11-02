class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = ""
        
        # Try removing each occurrence of digit
        for i in range(len(number)):
            if number[i] == digit:
                # Create candidate by removing digit at position i
                candidate = number[:i] + number[i+1:]
                # Update result if candidate is larger
                if candidate > result:
                    result = candidate
        
        return result
