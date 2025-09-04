# 104. Maximum Depth of Binary Tree

## Problem Description

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

### Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Example 2:
```
Input: root = [1,null,2]
Output: 2
```

## Constraints

- The number of nodes in the tree is in the range [0, 10^4].
- `-100 <= Node.val <= 100`

## Approach

Use recursive DFS:
1. If the node is null, depth is 0
2. Otherwise, depth is `1 + max(depth(left), depth(right))`

Time complexity: O(n)
Space complexity: O(h) where h is the height of the tree (recursion stack).
