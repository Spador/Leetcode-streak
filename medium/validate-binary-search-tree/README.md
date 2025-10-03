# 98. Validate Binary Search Tree

**Difficulty:** Medium

## Problem Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

## Examples

### Example 1:
```
Input: root = [2,1,3]
Output: true
```

### Example 2:
```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

## Constraints

- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

## Approach

The solution uses a recursive approach to validate the BST property. For each node, we maintain a range (left, right) that represents the valid range of values for that node.

### Algorithm:
1. Use a helper function that takes a node and its valid range (left, right)
2. Check if the current node's value is within the valid range
3. Recursively validate left subtree with range (left, node.val)
4. Recursively validate right subtree with range (node.val, right)
5. Return true only if all conditions are satisfied

### Time Complexity: O(n)
- We visit each node exactly once

### Space Complexity: O(h)
- Where h is the height of the tree (for recursion stack)
