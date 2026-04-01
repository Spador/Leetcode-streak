# 1022. Sum of Root To Leaf Binary Numbers

**Difficulty:** Easy

## Problem Description
Given a binary tree where each node has value 0 or 1, each root-to-leaf path represents a binary number. Return the sum of all such numbers.

## Examples

### Example 1
```
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
```

### Example 2
```
Input: root = [0]
Output: 0
```

## Constraints
- Number of nodes in `[1, 1000]`.
- `Node.val` is `0` or `1`.

## Approach
DFS passing the current accumulated value. At each node, shift left (`curr * 2`) and add `node.val`. At a leaf, return `curr`. Sum results from left and right subtrees.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(h)` where h is tree height
