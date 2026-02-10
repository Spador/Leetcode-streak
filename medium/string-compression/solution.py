# spador

class Solution:
    def compress(self, chars: List[str]) -> int:
        insert = 0
        i = 0
        while i < len(chars):
            group = 1
            while (i + group) < len(chars) and chars[i + group] == chars[i]:
                group += 1
            
            chars[insert] = chars[i]
            insert += 1
            if group > 1:
                num = str(group)
                for j in range(len(num)):
                    chars[insert] = num[j]
                    insert += 1
            i += group
        
        return insert
