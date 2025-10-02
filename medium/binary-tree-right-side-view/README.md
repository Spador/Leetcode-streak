# 199. Binary Tree Right Side View

**Difficulty:** Medium

## Problem Description

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Examples

### Example 1:
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

### Example 2:
```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

### Example 3:
```
Input: root = [1,null,3]
Output: [1,3]
```

### Example 4:
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Approach

The solution uses a breadth-first search (BFS) approach with a queue to traverse the binary tree level by level. For each level, we keep track of the rightmost node and add its value to the result.

### Algorithm:
1. Use a queue to perform level-order traversal
2. For each level, iterate through all nodes in that level
3. Keep track of the rightmost node in each level
4. Add the value of the rightmost node to the result
5. Continue until all levels are processed

### Time Complexity: O(n)
- We visit each node exactly once

### Space Complexity: O(w)
- Where w is the maximum width of the tree (maximum number of nodes at any level)
