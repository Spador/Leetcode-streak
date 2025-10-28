class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                # Push all characters except ']' to stack
                stack.append(s[i])
            else:
                # Extract substring between '[' and ']'
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                
                # Remove the opening bracket '['
                stack.pop()
                
                # Extract the number (can be multi-digit)
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                
                # Push the repeated substring back to stack
                stack.append(int(number) * substring)
        
        # Join all elements in stack to form final decoded string
        return "".join(stack)
