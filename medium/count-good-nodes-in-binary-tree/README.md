# 1448. Count Good Nodes in Binary Tree

**Difficulty:** Medium

## Problem Description

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

## Examples

### Example 1:
```
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
```

### Example 2:
```
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
```

### Example 3:
```
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
```

## Constraints

- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

## Approach

The solution uses a depth-first search (DFS) approach to traverse the binary tree. For each node, we keep track of the maximum value encountered in the path from root to the current node.

### Algorithm:
1. Use DFS to traverse the tree
2. For each node, check if its value is greater than or equal to the maximum value in the path from root
3. If yes, increment the count of good nodes
4. Update the maximum value for the current path
5. Recursively traverse left and right children
6. Return the total count of good nodes

### Time Complexity: O(n)
- We visit each node exactly once

### Space Complexity: O(h)
- Where h is the height of the tree (for recursion stack)
