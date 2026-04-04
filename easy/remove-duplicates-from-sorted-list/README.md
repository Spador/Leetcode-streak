# Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates so each element appears only once.

## Approach
- Use a single pointer traversing the list
- If current node's value equals the next node's value, skip the next node by updating the pointer
- Otherwise advance the pointer
- Return the original head

Time Complexity: O(n)
Space Complexity: O(1)
