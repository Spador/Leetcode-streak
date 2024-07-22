##spador

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        left = 0
        maxLen = 0

        for right in range(len(s)):
            charMap[s[right]] = 1 + charMap.get(s[right], 0)
            
            if (right - left + 1) - max(charMap.values()) > k:
                charMap[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
