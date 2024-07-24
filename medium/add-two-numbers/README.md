# 2. Add Two Numbers

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Examples

### Example 1:
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

### Example 2:
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3:
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

## Constraints

- The number of nodes in each linked list is in the range [1, 100].
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Approach

The solution uses **digit-by-digit addition with carry**:

1. **Initialize**: Create a dummy head node and a carry variable
2. **Iterate**: While either list has nodes or there's a carry
3. **Add Digits**: 
   - Get values from both lists (0 if list is exhausted)
   - Add them along with the carry
   - Calculate new carry and digit value
4. **Create Node**: Create a new node with the calculated digit
5. **Update Pointers**: Move to the next nodes in both lists
6. **Return Result**: Return the head of the result list

**Key Insight**: Process both lists simultaneously, handling different lengths by treating exhausted lists as having value 0.

## Time Complexity

O(max(m, n)) where m and n are the lengths of the input lists.

## Space Complexity

O(max(m, n)) - Space needed for the result list.
