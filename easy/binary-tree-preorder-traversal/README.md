# 144. Binary Tree Preorder Traversal

**Difficulty:** Easy

## Problem Description
Given the root of a binary tree, return the preorder traversal of its nodes' values.

## Examples

### Example 1
```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

### Example 2
```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
```

## Constraints
- Number of nodes in `[0, 100]`.
- `-100 <= Node.val <= 100`

## Approach
Iterative: use a stack, push the right child before going left. At each step, record the current node's value, push its right child, then move to the left child.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
