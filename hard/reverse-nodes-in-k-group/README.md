# 25. Reverse Nodes in k-Group

## Problem Description

Given the head of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

## Examples

### Example 1:
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

### Example 2:
```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

## Constraints

- The number of nodes in the list is `n`.
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`

## Follow-up

Can you solve the problem in O(1) extra memory space?

## Approach

Use iterative group reversal with a helper to find each group’s `k`th node:

1. Use a dummy `start` node pointing to `head`
2. For each group, find the `k`th node using `getKth`
3. Reverse the nodes in the group by standard in-place linked list reversal
4. Reconnect the reversed group with the previous and next parts
5. Move `groupPrev` to the end of the reversed group and continue

Time complexity: O(n)
Space complexity: O(1)
