# Evaluate Reverse Polish Notation

Evaluate an arithmetic expression given in Reverse Polish Notation.

## Approach
- Use a stack; push operands as integers
- On encountering an operator, pop two operands (b then a), apply the operator, and push the result
- Use int(a / b) for division to truncate toward zero
- Return the single remaining value on the stack

Time Complexity: O(n)
Space Complexity: O(n)
