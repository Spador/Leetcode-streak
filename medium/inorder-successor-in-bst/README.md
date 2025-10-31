# 285. Inorder Successor in BST

**Difficulty:** Medium

## Problem Description

Given the root of a binary search tree and a node `p` in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node `p` is the node with the smallest key greater than `p.val`.

## Examples

### Example 1:
```
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
```

### Example 2:
```
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
```

## Constraints

- The number of nodes in the tree is in the range [1, 10⁴].
- -10⁵ <= Node.val <= 10⁵
- All Nodes will have unique values.

## Approach

This problem can be solved using a binary search approach:

1. **Binary Search**: Traverse the BST similar to binary search
2. **Successor Tracking**: Keep track of potential successor while traversing
3. **Two Cases**:
   - If `p.val >= root.val`: Successor must be in right subtree
   - If `p.val < root.val`: Current root is a potential successor, but check left subtree for smaller one

## Algorithm

1. Initialize `successor` to None
2. While root is not null:
   - If `p.val >= root.val`:
     - Move to right subtree (successor must be there)
   - Else:
     - Current root is a potential successor
     - Update successor to current root
     - Move to left subtree to find smaller successor
3. Return successor

## Implementation Details

- **Binary Search Traversal**: Similar to searching in BST
- **Successor Tracking**: Maintain potential successor during traversal
- **Value Comparison**: Compare node values to decide direction
- **Early Termination**: Stop when root becomes null

## Key Optimizations

- **O(h) Time**: Height of tree in worst case
- **O(1) Space**: Only uses constant extra space
- **Single Pass**: Traverses tree once
- **No Recursion**: Iterative approach

## Time Complexity

- **Time**: O(h) where h is the height of the tree
  - In worst case (skewed tree), O(n)
  - In balanced tree, O(log n)
- **Space**: O(1) for the traversal

## Solution

The solution uses binary search approach:
- Traverses BST similar to binary search
- Tracks potential successor during traversal
- Returns the in-order successor or null if none exists
