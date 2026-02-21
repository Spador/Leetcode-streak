# 234. Palindrome Linked List

**Difficulty:** Easy

## Problem Description
Given the head of a singly linked list, return `true` if it is a palindrome, `false` otherwise.

## Examples

### Example 1
```
Input: head = [1,2,2,1]
Output: true
```

### Example 2
```
Input: head = [1,2]
Output: false
```

## Constraints
- Number of nodes in `[1, 10^5]`
- `0 <= Node.val <= 9`

## Approach
1. Use slow/fast pointers to find the middle of the list.
2. Reverse the second half in-place.
3. Compare the first half with the reversed second half node by node.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
