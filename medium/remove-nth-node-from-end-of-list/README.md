# 19. Remove Nth Node From End of List

## Problem Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Examples

### Example 1:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

### Example 2:
```
Input: head = [1], n = 1
Output: []
```

### Example 3:
```
Input: head = [1,2], n = 1
Output: [1]
```

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Follow up

Could you do this in one pass?

## Approach

The solution uses the **two-pointer technique** with a dummy node:

1. **Create a dummy node**: Points to the head to handle edge cases
2. **Initialize pointers**: 
   - `slow` starts at dummy
   - `fast` starts at head
3. **Move fast pointer**: Advance `fast` by `n` positions
4. **Move both pointers**: Move `slow` and `fast` together until `fast` reaches the end
5. **Remove the node**: `slow.next = slow.next.next`
6. **Return result**: Return `dummy.next`

**Key Insight**: When `fast` reaches the end, `slow` will be pointing to the node before the one we want to remove.

## Time Complexity

O(n) - Single pass through the linked list.

## Space Complexity

O(1) - Only using a constant amount of extra space.
