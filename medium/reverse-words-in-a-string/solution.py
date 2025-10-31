class Solution:
    def reverseWords(self, s: str) -> str:
        words = [""]
        word = ""
        s += " "  # Add trailing space to handle last word
        
        for c in s:
            if c != " ":
                # Build word character by character
                word += c
            if c == " ":
                if len(word) > 0:
                    # Add word and space separator to list
                    words.append(word)
                    words.append(" ")
                    word = ""
                else:
                    # Skip multiple consecutive spaces
                    continue
        
        # Reverse the list (excluding first empty string and last space)
        # Join and return the reversed words
        return "".join(words[-2:0:-1])
