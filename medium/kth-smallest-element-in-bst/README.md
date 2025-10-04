# 230. Kth Smallest Element in a BST

## Problem Description

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

## Examples

### Example 1:
```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### Example 2:
```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Constraints

- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

## Follow up

If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

## Approach

The solution uses an iterative inorder traversal of the BST. Since BST properties guarantee that an inorder traversal visits nodes in ascending order, we can simply count nodes during the traversal until we reach the kth node.

### Algorithm:
1. Use a stack to perform iterative inorder traversal
2. Keep a counter to track the number of nodes visited
3. When the counter reaches k, return the current node's value
4. Continue traversal if kth element not found yet

### Time Complexity: O(h + k)
- Where h is the height of the tree
- In the worst case (skewed tree), O(n + k) = O(n)

### Space Complexity: O(h)
- Where h is the height of the tree for the stack
- In the worst case (skewed tree), O(n)
