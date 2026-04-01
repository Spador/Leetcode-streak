# Implement Queue using Stacks

Implement a FIFO queue using only two stacks, supporting push, pop, peek, and empty operations.

## Approach
- Use two stacks (stack1 for push, stack2 for pop/peek) and a flag to track current mode
- On push: if in push mode, append to stack1; if in pop mode, transfer stack2 back to stack1 first
- On pop/peek: if in push mode, transfer all of stack1 to stack2 and switch to pop mode, then pop/peek from stack2
- empty: check combined size of both stacks

Time Complexity: O(1) amortized per operation
Space Complexity: O(n)
