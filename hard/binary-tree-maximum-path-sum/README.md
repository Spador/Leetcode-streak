# 124. Binary Tree Maximum Path Sum

## Problem Description

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

## Examples

### Example 1:
```
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

### Example 2:
```
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

## Constraints

- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000

## Approach

The solution uses a recursive DFS approach with a global maximum tracker. The key insight is to consider two types of paths at each node:

1. **Path through current node**: This includes the current node and can extend to both left and right subtrees
2. **Path ending at current node**: This includes the current node and extends to only one subtree (left or right)

### Algorithm:
1. Use DFS to traverse the tree
2. For each node, calculate the maximum path sum that can be extended from that node (to parent)
3. Update the global maximum with the maximum path sum that goes through the current node
4. Return the maximum path sum that can be extended from the current node

### Key Points:
- Use `max(0, left)` and `max(0, right)` to handle negative subtree sums
- The global maximum considers paths that go through the current node (left + node + right)
- The return value considers paths that can be extended upward (node + max(left, right))

### Time Complexity: O(n)
- We visit each node exactly once

### Space Complexity: O(h)
- Where h is the height of the tree (recursion stack depth)
- In the worst case (skewed tree), O(n)
