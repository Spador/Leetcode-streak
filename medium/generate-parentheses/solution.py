# spador

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open if number of open < n
        # add closed if number of closed < number of open
        # valid iff number of open == number of closed == n

        stack = []
        result = []

        def backtrack(openP, closeP):
            if openP == closeP == n:
                result.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                backtrack(openP + 1, closeP)
                stack.pop()
            
            if closeP < openP:
                stack.append(")")
                backtrack(openP, closeP + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result


