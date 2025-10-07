# 297. Serialize and Deserialize Binary Tree

## Problem Description

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

**Clarification:** The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

## Examples

### Example 1:
```
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
```

### Example 2:
```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000

## Approach

The solution uses a **preorder traversal (DFS)** approach for both serialization and deserialization:

### Serialization:
1. Use preorder traversal (root → left → right)
2. For each node, append its value to the result
3. For null nodes, append "N" (or any marker)
4. Join all values with commas to create the final string

### Deserialization:
1. Split the serialized string by commas
2. Use a global index to track current position
3. Recursively build the tree using preorder traversal
4. When encountering "N", return null
5. Otherwise, create a new node and recursively build left and right subtrees

### Key Insights:
- **Preorder traversal** is ideal because the root is always first, making reconstruction straightforward
- **Null markers** are essential to preserve tree structure
- **Global index** in deserialization ensures we process nodes in the correct order

### Time Complexity: O(n)
- Both serialization and deserialization visit each node exactly once

### Space Complexity: O(n)
- Recursion stack depth: O(h) where h is tree height
- Serialized string storage: O(n)
- In worst case (skewed tree): O(n)

## Alternative Approaches
- **BFS (Level-order traversal)**: Can also be used for serialization/deserialization
- **Inorder + Preorder**: More complex but possible
- **Postorder**: Also viable with proper handling
