# spador

from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            count = defaultdict(int)

            for j in range(i, len(s)):
                if s[j] not in count:
                    count[s[j]] = 1
                else:
                    count[s[j]] += 1
                
                if len(set(count.values())) == 1:
                    result = max(result, j - i + 1)
        return result
