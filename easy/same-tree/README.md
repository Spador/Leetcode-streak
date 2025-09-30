# 100. Same Tree

## Problem Description

Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

## Examples

### Example 1:
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

### Example 2:
```
Input: p = [1,2], q = [1,null,2]
Output: false
```

### Example 3:
```
Input: p = [1,2,1], q = [1,1,2]
Output: false
```

## Constraints

- The number of nodes in both trees is in the range [0, 100].
- `-10^4 <= Node.val <= 10^4`

## Approach

Use recursive comparison:
1. If both nodes are null, they are the same (base case)
2. If one is null or values differ, they are not the same
3. Recursively check left and right subtrees
4. Both subtrees must be the same for the trees to be identical

Time complexity: O(min(m,n)) where m and n are the number of nodes in the trees
Space complexity: O(min(m,n)) due to recursion stack
