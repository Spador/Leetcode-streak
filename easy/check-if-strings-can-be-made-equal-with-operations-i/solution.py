# spador

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        p1, p2 = 0, 0
        s1, s2 = list(s1), list(s2)
        while p1 < 4 and p2 < 4:
            if s1[p1] != s2[p2]:
                if p1 + 2 < 4 and s1[p1 + 2] == s2[p2]:
                    s1[p1], s1[p1 + 2] = s1[p1 + 2], s1[p1]
                else:
                    return False
            p1 += 1
            p2 += 1
        return True
