# 143. Reorder List

## Problem Description

You are given the head of a singly linked-list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

Reorder the list to be on the following form:

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Examples

### Example 1:
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

### Example 2:
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Constraints

- The number of nodes in the list is in the range [1, 5 * 10^4].
- `1 <= Node.val <= 1000`

## Approach

The solution uses a **three-step process**:

1. **Find the middle**: Use slow and fast pointers to find the middle of the list
2. **Reverse the second half**: Reverse the links in the second half of the list
3. **Merge the two halves**: Interleave the nodes from the first and second halves

**Step-by-step breakdown**:
- Use slow/fast pointer technique to find the middle node
- Split the list at the middle and reverse the second half
- Merge the two halves by alternating between first and second half nodes

**Key Insight**: The reordered list alternates between nodes from the first half and reversed second half.

## Time Complexity

O(n) - Single pass to find middle, reverse second half, and merge.

## Space Complexity

O(1) - Only using a constant amount of extra space for pointers.
