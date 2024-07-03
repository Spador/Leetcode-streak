class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        hashmap = {}
        
        for i,c in enumerate(s):
            if c in hashmap and start <= hashmap[c]:
                start = hashmap[c]+1
            
            else:
                max_length = max(i-start+1, max_length)
            
            hashmap[c] = i
        
        return max_length 