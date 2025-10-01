# 102. Binary Tree Level Order Traversal

## Problem Description

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Examples

### Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

### Example 2:
```
Input: root = [1]
Output: [[1]]
```

### Example 3:
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 2000].
- `-1000 <= Node.val <= 1000`

## Approach

Use BFS with a queue:
1. Use a deque to store nodes for level-by-level processing
2. For each level, process all nodes currently in the queue
3. Add node values to the current level list
4. Add left and right children to the queue for the next level
5. Add the level list to result if it's not empty

Time complexity: O(n) where n is the number of nodes
Space complexity: O(w) where w is the maximum width of the tree
