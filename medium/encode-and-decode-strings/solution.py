#spador
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Encoding by adding length of each string followed by delimeter '$'
        result = ""
        for i in strs:
            result += str(len(i)) + "$" + i
        return result
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result = []
        i = 0
        
        while i < len(s):
            count = int(s[i])
            while s[i+1] != "$":
                count = count*10 + int(s[i+1])
                i += 1
            word = ""
            for j in range(i+2,i+2+count):
                word += s[j]
            result.append(word)
            i += 2 + count
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
