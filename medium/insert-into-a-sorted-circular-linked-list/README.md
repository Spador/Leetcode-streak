# 708. Insert into a Sorted Circular Linked List

Insert a value into a sorted circular linked list while maintaining the sorted order.

## Approach
- Handle the empty list edge case by creating a self-referencing node
- Traverse the circular list looking for the correct insertion point
- Three cases: normal range (curr <= insertVal <= next), boundary crossing (curr > next and insertVal is outside the mid range), or full loop (all equal values)
- Insert the new node between curr and curr.next

Time Complexity: O(n)
Space Complexity: O(1)
