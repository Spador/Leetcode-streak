# spador

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        hashset = set()

        for l, r in zip(range(0, len(s) - k + 1), range(k, len(s) + 1)):
            hashset.add(s[l:r])
        
        return len(hashset) == (1<<k)
