# spador

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for c in magazine:
            if c not in mag:
                mag[c] = 1
            else:
                mag[c] += 1

        for letter in ransomNote:
            if letter not in mag or mag[letter] == 0:
                return False
            else:
                mag[letter] -= 1
        return True
