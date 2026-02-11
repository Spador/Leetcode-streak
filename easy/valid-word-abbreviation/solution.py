# spador

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w, a = 0, 0     # w = word pointer, a = abbr pointer

        while w < len(word) and a < len(abbr):
            if word[w] == abbr[a]:
                w += 1
                a += 1

            elif abbr[a].isalpha() or abbr[a] == "0":
                return False
            
            else:
                num = 0
                while a < len(abbr) and not abbr[a].isalpha():
                    num = (10 * num) + int(abbr[a])
                    a += 1
                w += num
        
        return w == len(word) and a == len(abbr)
