# 545. Boundary of Binary Tree

**Difficulty:** Medium

## Problem Description
The **boundary** of a binary tree is the concatenation of the **root**, the **left boundary**, the **leaves** ordered from left-to-right, and the **reverse order** of the **right boundary**.

**Left boundary:** The root's left child is in the left boundary. If the root has no left child, the left boundary is empty. From there: if a node in the left boundary has a left child, that left child is in the left boundary; if it has no left but has a right child, the right child is in the left boundary. The **leftmost leaf is not** in the left boundary.

**Right boundary:** Same idea on the right side of the root's right subtree. The rightmost leaf is not part of the right boundary. The right boundary is empty if the root has no right child.

**Leaves:** Nodes with no children. The root is not considered a leaf for this problem.

Given the `root` of a binary tree, return the values of its boundary.

## Examples

### Example 1
```
Input: root = [1,null,2,3,4]
Output: [1,3,4,2]
Explanation:
- The left boundary is empty because the root does not have a left child.
- The right boundary follows the path starting from the root's right child 2 -> 4. 4 is a leaf, so the right boundary is [2].
- The leaves from left to right are [3,4].
Concatenating everything results in [1] + [] + [3,4] + [2] = [1,3,4,2].
```

### Example 2
```
Input: root = [1,2,3,4,5,6,null,null,null,7,8,9,10]
Output: [1,2,4,7,8,9,10,6,3]
Explanation:
- The left boundary follows the path starting from the root's left child 2 -> 4. 4 is a leaf, so the left boundary is [2].
- The right boundary follows the path starting from the root's right child 3 -> 6 -> 10. 10 is a leaf, so the right boundary is [3,6], and in reverse order is [6,3].
- The leaves from left to right are [4,7,8,9,10].
Concatenating everything results in [1] + [2] + [4,7,8,9,10] + [6,3] = [1,2,4,7,8,9,10,6,3].
```

## Constraints
- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-1000 <= Node.val <= 1000`

## Approach
1. **Root:** Add `root.val` first (handle single-node tree by returning `[root.val]`).
2. **Left boundary:** From `root.left`, go down always preferring left child, then right if no left; add only non-leaf nodes.
3. **Leaves:** DFS (in-order) to collect all leaf values left to right.
4. **Right boundary:** From `root.right`, go down always preferring right child, then left if no right; collect non-leaf nodes in a temp list, then append in **reverse** to the result.

## Time & Space Complexity
- **Time Complexity:** O(n) — each node visited a constant number of times.
- **Space Complexity:** O(n) for recursion stack and the right-boundary temp list.
