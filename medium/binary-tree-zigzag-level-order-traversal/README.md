# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium

## Problem Description
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values (left to right, then right to left for the next level, alternating between).

## Examples

### Example 1
```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

### Example 2
```
Input: root = [1]
Output: [[1]]
```

### Example 3
```
Input: root = []
Output: []
```

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`
- `-100 <= Node.val <= 100`

## Approach
BFS with a direction flag:
1. Use a deque for standard level-order traversal.
2. Track a `revflag` boolean to determine direction for each level.
3. On normal levels, append node values to the end of the level list.
4. On reverse levels, prepend node values to the front — effectively reversing the order without an extra reverse pass.
5. Flip `revflag` after each level.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — every node is visited once.
- **Space Complexity:** `O(n)` — deque holds at most one full level at a time, up to `n/2` nodes.
