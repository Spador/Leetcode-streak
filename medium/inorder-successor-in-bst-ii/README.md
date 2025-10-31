# 510. Inorder Successor in BST II

**Difficulty:** Medium

## Problem Description

Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than `node.val`.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

```python
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

## Examples

### Example 1:
```
Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
```

### Example 2:
```
Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
```

## Constraints

- The number of nodes in the tree is in the range [1, 10⁴].
- -10⁵ <= Node.val <= 10⁵
- All Nodes will have unique values.

## Follow-up

Could you solve it without looking up any of the node's values?

## Approach

This problem can be solved using two cases:

1. **Right Subtree Exists**: If the node has a right child, the successor is the leftmost node in the right subtree
2. **No Right Subtree**: If the node has no right child, traverse up the parent chain until we find a parent where the current node is in the left subtree

## Algorithm

1. **Case 1 - Right child exists**:
   - Move to the right child
   - Traverse to the leftmost node in the right subtree
   - Return that node
2. **Case 2 - No right child**:
   - Traverse up the parent chain
   - While current node is the right child of its parent, keep moving up
   - Return the parent when current node is in left subtree (or null if no such parent exists)

## Implementation Details

- **Right Subtree Check**: First check if node has a right child
- **Leftmost Node**: Find the minimum value in right subtree
- **Parent Traversal**: Move up until finding a parent with current node in left subtree
- **Null Handling**: Return null if no successor exists

## Key Optimizations

- **Two Case Handling**: Efficiently handles both scenarios
- **O(h) Time**: Height of tree in worst case
- **O(1) Space**: Only uses constant extra space
- **No Value Lookup**: Solves without comparing node values (follow-up requirement)

## Time Complexity

- **Time**: O(h) where h is the height of the tree
  - In worst case, traverse from leaf to root
- **Space**: O(1) for the traversal

## Solution

The solution uses two-case approach:
- If right subtree exists, finds leftmost node in right subtree
- Otherwise, traverses up parent chain to find successor
- Returns the in-order successor or null if none exists
