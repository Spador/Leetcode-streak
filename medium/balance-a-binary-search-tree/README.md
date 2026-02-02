# 1382. Balance a Binary Search Tree

**Difficulty:** Medium

## Problem Description
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

## Examples

### Example 1
```
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
```

### Example 2
```
Input: root = [2,1,3]
Output: [2,1,3]
```

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `1 <= Node.val <= 10^5`.

## Approach
We use the fact that an **in-order traversal** of a BST yields the node values in sorted order.

1. Perform an in-order traversal of the given BST and collect the **nodes themselves** (not just their values) in an array `arr`.
2. Rebuild a balanced BST from the sorted array:
   - Use a recursive function `balance(l, r)` that:
     - If `l > r`, returns `None`.
     - Picks the middle index `m = (l + r) // 2` as the root of this subtree.
     - Recursively builds the left subtree from `[l, m - 1]` and the right subtree from `[m + 1, r]`.
     - Sets `arr[m].left` and `arr[m].right` to these subtrees and returns `arr[m]` as the root.
3. The rebuilt tree is height-balanced because we always choose the middle element as the root at each step.

This preserves all original node values and satisfies the BST property.

## Time & Space Complexity
- **Time Complexity:** `O(N)`, where `N` is the number of nodes — one in-order traversal plus one pass to build the balanced tree.
- **Space Complexity:** `O(N)` for storing the nodes in the array and `O(H)` recursion stack (where `H` is the height of the balanced tree, `O(log N)` on average).
