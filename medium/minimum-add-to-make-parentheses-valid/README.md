# 921. Minimum Add to Make Parentheses Valid

Return the minimum number of insertions to make a parentheses string valid.

## Approach
- Use a stack to track unmatched parentheses
- For each character, if it's `)` and the top of the stack is `(`, pop (matched pair found)
- Otherwise, push the character onto the stack
- The remaining stack size is the number of unmatched parentheses that need to be added

Time Complexity: O(n)
Space Complexity: O(n)
