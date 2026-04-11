# spador

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map, s2_map = {}, {}
        for asci in range(ord("a"), ord("z") + 1):
            s1_map[chr(asci)] = 0
            s2_map[chr(asci)] = 0

        for i in range(len(s1)):
            s1_map[s1[i]] += 1
            s2_map[s2[i]] += 1

        matching = 0
        for ch in s1_map:
            if s1_map[ch] == s2_map[ch]:
                matching += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matching == 26:
                return True

            s2_map[s2[right]] += 1
            if s2_map[s2[right]] == s1_map[s2[right]]:
                matching += 1
            elif s2_map[s2[right]] == s1_map[s2[right]] + 1:
                matching -= 1

            s2_map[s2[left]] -= 1
            if s2_map[s2[left]] == s1_map[s2[left]]:
                matching += 1
            elif s2_map[s2[left]] + 1 == s1_map[s2[left]]:
                matching -= 1

            left += 1

        return matching == 26
