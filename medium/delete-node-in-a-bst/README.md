# 450. Delete Node in a BST

**Difficulty:** Medium

## Problem Description

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

## Examples

### Example 1:
```
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
```

### Example 2:
```
Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
```

### Example 3:
```
Input: root = [], key = 0
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 10⁴].
- -10⁵ <= Node.val <= 10⁵
- Each node has a unique value.
- root is a valid binary search tree.
- -10⁵ <= key <= 10⁵

## Follow-up

Could you solve it with time complexity O(height of tree)?

## Approach

This problem can be solved using recursive deletion with three cases:

1. **Node Not Found**: If key doesn't match, recursively search left or right subtree
2. **Node with 0 or 1 Child**: Replace node with its child (or None)
3. **Node with 2 Children**: Replace node value with inorder successor (minimum in right subtree), then delete the successor

## Algorithm

1. If root is null, return null
2. If key > root.val, recursively delete from right subtree
3. If key < root.val, recursively delete from left subtree
4. If key == root.val (node found):
   - If no left child, return right child
   - If no right child, return left child
   - If both children exist:
     - Find minimum value in right subtree (inorder successor)
     - Replace root value with successor value
     - Recursively delete the successor from right subtree
5. Return root

## Implementation Details

- **Recursive Approach**: Use recursion to traverse and modify tree
- **Three Cases**: Handle node with 0, 1, or 2 children
- **Inorder Successor**: Find minimum in right subtree for replacement
- **Tree Modification**: Update child pointers during deletion

## Key Optimizations

- **O(h) Time**: Height of tree in worst case
- **Recursive Structure**: Clean and intuitive implementation
- **Inorder Successor**: Maintains BST property after deletion
- **Follow-up Requirement**: Meets O(height) time complexity

## Time Complexity

- **Time**: O(h) where h is the height of the tree
  - In worst case (skewed tree), O(n)
  - In balanced tree, O(log n)
- **Space**: O(h) for recursion stack

## Solution

The solution uses recursive deletion:
- Searches for the node to delete
- Handles three deletion cases (0, 1, or 2 children)
- Uses inorder successor for nodes with two children
- Returns the updated root
