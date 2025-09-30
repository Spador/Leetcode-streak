# 572. Subtree of Another Tree

## Problem Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

## Examples

### Example 1:
```
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

### Example 2:
```
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

## Constraints

- The number of nodes in the root tree is in the range [1, 2000].
- The number of nodes in the subRoot tree is in the range [1, 1000].
- `-10^4 <= root.val <= 10^4`
- `-10^4 <= subRoot.val <= 10^4`

## Approach

Use recursive approach with helper function:
1. If `subRoot` is null, it's always a subtree (base case)
2. If `root` is null but `subRoot` isn't, it's not a subtree
3. Check if current `root` matches `subRoot` using helper function
4. Recursively check left and right subtrees of `root`
5. Helper function `sameTree` compares two trees for identical structure and values

Time complexity: O(m×n) where m and n are the number of nodes in root and subRoot
Space complexity: O(h) where h is the height of the root tree (recursion stack)
