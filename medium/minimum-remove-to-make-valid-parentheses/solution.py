# spador

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = [""] * len(s)
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if not stack:
                    continue
                else:
                    result[stack.pop()] = "("
                    result[i] = ")"
            else:
                result[i] = ch

        return "".join(result)
