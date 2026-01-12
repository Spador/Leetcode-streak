# 129. Sum Root to Leaf Numbers

**Difficulty:** Medium

## Problem Description
You are given the root of a binary tree containing digits from `0` to `9` only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path `1 -> 2 -> 3` represents the number `123`.

Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

## Examples

### Example 1
```
Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```

### Example 2
```
Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

## Constraints
- The number of nodes in the tree is in the range `[1, 1000]`.
- `0 <= Node.val <= 9`
- The depth of the tree will not exceed `10`.

## Approach
We perform a **DFS traversal** where we carry along the numeric value formed by the current root-to-node path.

At each node:
- Let `num` be the integer formed so far on the path from the root to the current node.
- When we go to a child, the new value becomes `num * 10 + node.val`.
- When we reach a **leaf node** (no left and right children), we return the complete number for that path.
- For internal nodes, we sum the values returned by the left and right subtrees.

Algorithm:
1. Define a helper function `dfs(curr, num)`:
   - If `curr` is `None`, return `0` (no number contributed).
   - Update `num = num * 10 + curr.val`.
   - If `curr` is a leaf (`not curr.left and not curr.right`), return `num`.
   - Otherwise, return `dfs(curr.left, num) + dfs(curr.right, num)`.
2. Call `dfs(root, 0)` and return its result.

This way, every root-to-leaf path contributes exactly one integer to the total sum.

## Time & Space Complexity
- **Time Complexity:** `O(N)` where `N` is the number of nodes, since each node is visited once.
- **Space Complexity:** `O(H)` for the recursion stack, where `H` is the height of the tree (at most 10 by constraint).

