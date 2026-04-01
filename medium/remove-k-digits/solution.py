# spador

# Use a monotonic stack. It means we can append only in ascending order.
# if there is a bigger number on top of the stack and k > 0, then we pop the top.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for ch in num:
            while stack and k > 0 and (int(ch) < int(stack[-1])):
                stack.pop()
                k -= 1
            stack.append(ch)
        stack = stack[:len(stack) - k]
        result = "".join(stack).lstrip("0")
        return result if result else "0"
