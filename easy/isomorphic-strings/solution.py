# spador

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Smap = {}
        Tmap = {}
        for i in range(len(s)):
            if s[i] not in Smap:
                Smap[s[i]] = t[i]
            else:
                if Smap[s[i]] != t[i]:
                    return False
            if t[i] not in Tmap:
                Tmap[t[i]] = s[i]
            else:
                if Tmap[t[i]] != s[i]:
                    return False
        return True
