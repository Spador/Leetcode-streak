class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Using DP: Top Down Memoization
        Cache = {}
        
        def dfs(i, j):
            # Check if result already computed
            if (i, j) in Cache:
                return Cache[(i, j)]
            
            # Base case: both string and pattern exhausted
            if i >= len(s) and j >= len(p):
                return True
            
            # Base case: pattern exhausted but string isn't
            if j >= len(p):
                return False
            
            # Check if current characters match
            Match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            # Handle '*' character (matches zero or more of preceding element)
            if (j + 1) < len(p) and p[j + 1] == "*":
                # Two choices:
                # 1. Don't use '*' (skip the pattern)
                # 2. Use '*' (match one or more characters)
                Cache[(i, j)] = (dfs(i, j + 2) or           # if we don't use *
                                 (Match and dfs(i + 1, j))) # if we use *
                return Cache[(i, j)]
            
            # If characters match, advance both indices
            if Match:
                Cache[(i, j)] = dfs(i + 1, j + 1)
                return Cache[(i, j)]
            
            # No match found
            Cache[(i, j)] = False
            return Cache[(i, j)]
        
        return dfs(0, 0)
