# spador

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}               # store last occurance of each character
        size, currEnd = 0, 0
        result = []
        for i in range(len(s)):
                last[s[i]] = i
        
        for i in range(len(s)):
            size += 1
            if currEnd < last[s[i]]:
                currEnd = last[s[i]]
            if i == currEnd:
                result.append(size)
                size = 0
            if (i != len(s) - 1) and (currEnd == len(s) - 1):           # Optimization
                result.append(currEnd - i + size)
                return result

        return result

