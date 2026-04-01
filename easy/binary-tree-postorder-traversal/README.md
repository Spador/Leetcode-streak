# 145. Binary Tree Postorder Traversal

**Difficulty:** Easy

## Problem Description
Given the root of a binary tree, return the postorder traversal of its nodes' values.

## Examples

### Example 1
```
Input: root = [1,null,2,3]
Output: [3,2,1]
```

### Example 2
```
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,6,7,5,2,9,8,3,1]
```

## Constraints
- Number of nodes in `[0, 100]`.
- `-100 <= Node.val <= 100`

## Approach
Iterative using a stack with a visited flag. Push a node unvisited first; when popped unvisited, re-push it as visited then push right and left children unvisited. When popped visited, append to result.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
