# Basic Calculator II

Evaluate a mathematical expression string containing integers and operators (+, -, *, /).

## Approach
- Use stack to handle operator precedence
- Process numbers and operators in one pass
- For multiplication and division, apply immediately
- For addition and subtraction, store in stack
- Sum all values in stack at the end

Time Complexity: O(n)
Space Complexity: O(n) 