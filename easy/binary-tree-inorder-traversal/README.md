# 94. Binary Tree Inorder Traversal

**Difficulty:** Easy

## Problem Description
Given the root of a binary tree, return the inorder traversal of its nodes' values.

## Examples

### Example 1
```
Input: root = [1,null,2,3]
Output: [1,3,2]
```

### Example 2
```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]
```

## Constraints
- Number of nodes in `[0, 100]`.
- `-100 <= Node.val <= 100`

## Approach
Iterative: push all left children onto the stack first. Then pop, record value, and move to the right child.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
