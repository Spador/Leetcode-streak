# Middle of the Linked List

Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second one.

## Approach
- Use slow and fast pointers, both starting at head
- Move slow one step and fast two steps each iteration
- When fast reaches the end, slow is at the middle
- Naturally returns the second middle node for even-length lists

Time Complexity: O(n)
Space Complexity: O(1)
