class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = [""] * len(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    res[stack.pop()] = '('
                    res[i] = char
            else:
                res[i] = char
        return ''.join(res) 