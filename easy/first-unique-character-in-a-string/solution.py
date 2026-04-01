# spador

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(int)
        for ch in s:
            hashmap[ch] += 1
        
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1
