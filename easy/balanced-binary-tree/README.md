# 110. Balanced Binary Tree

## Problem Description

Given a binary tree, determine if it is height-balanced.

## Examples

### Example 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

### Example 2:
```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

### Example 3:
```
Input: root = []
Output: true
```

## Constraints

- The number of nodes in the tree is in the range [0, 5000].
- `-10^4 <= Node.val <= 10^4`

## Approach

Use DFS that returns both balance status and height:
1. For each node, recursively check if left and right subtrees are balanced
2. A tree is balanced if both subtrees are balanced AND the height difference is ≤ 1
3. Return `[isBalanced, height]` for each subtree
4. The root is balanced if the final result's balance flag is true

Time complexity: O(n)
Space complexity: O(h) where h is the height of the tree (recursion stack).
