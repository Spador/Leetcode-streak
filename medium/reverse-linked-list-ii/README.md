# 92. Reverse Linked List II

**Difficulty:** Medium

## Problem Description
Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the reversed list.

## Examples

### Example 1
```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
```

### Example 2
```
Input: head = [5], left = 1, right = 1
Output: [5]
```

## Constraints
- The number of nodes in the list is `n`.
- `1 <= n <= 500`
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

## Follow-up
Could you do it in one pass?

## Approach
Use a one-pass in-place reversal with a dummy node:

1. Create a `dummy` node pointing to `head`.
2. Walk `left - 1` steps from `dummy` to find `leftPrev` (node before the sublist) and `curr` (node at position `left`).
3. Reverse the next `right - left + 1` nodes using standard linked list reversal, keeping track of `prev` and `curr`.
4. After reversal, `prev` is the new head of the sublist and `leftPrev.next` is the tail; reconnect:
   - `leftPrev.next.next = curr` (tail points to the node after position `right`).
   - `leftPrev.next = prev` (link node before sublist to new head of sublist).
5. Return `dummy.next`.

## Time & Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1) extra space.
