# spador

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'I', 'U'}

        words = sentence.split()
        result = []
        for i, w in enumerate(words, 1):
            temp = ""
            if w[0] not in vowels:
                temp += w[1:] + w[0]
            else:
                temp += w
            temp += 'ma'
            temp += ('a' * i)
            result.append(temp)
        return " ".join(result)
