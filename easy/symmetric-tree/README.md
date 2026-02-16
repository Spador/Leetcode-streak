# 101. Symmetric Tree

**Difficulty:** Easy

## Problem Description
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

## Examples

### Example 1
```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

### Example 2
```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`
- `-100 <= Node.val <= 100`

## Approach

### Recursive
1. Define a helper `dfs(left, right)` that checks if two subtrees are mirrors.
2. Two nodes are mirrors if their values match and `left.left` mirrors `right.right`, and `left.right` mirrors `right.left`.
3. Base cases: both null → True; one null → False.

### Iterative
1. Use a deque, initializing with `[root, root]`.
2. Pop two nodes at a time and compare their values.
3. Push children in mirror order: `(t1.left, t2.right)` and `(t1.right, t2.left)`.
4. Continue until the queue is empty — return True.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — every node is visited once.
- **Space Complexity:** `O(n)` — recursion stack / deque can hold up to `n` nodes in the worst case.
