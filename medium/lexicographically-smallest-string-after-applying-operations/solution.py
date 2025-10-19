class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        n = len(s)

        # Building a map of each digit if 'a' is added to it.
        incrementMap = {str(n): str((n + a) % 10) for n in range(10)}

        def addOdd(s):
            res = ""
            for i in range(n):
                if i % 2 == 0:
                    res += s[i]
                else:
                    res += incrementMap[s[i]]
            return res
        
        def rotate(s):
            return s[n-b:] + s[:n-b]

        seen = set()

        def dfs(s):
            if s in seen:
                return
            seen.add(s)
            dfs(addOdd(s))
            dfs(rotate(s))
            return
        
        dfs(s)
        return min(seen)
