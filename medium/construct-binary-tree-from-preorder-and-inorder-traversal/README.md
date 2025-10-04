# 105. Construct Binary Tree from Preorder and Inorder Traversal

## Problem Description

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

## Examples

### Example 1:
```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

### Example 2:
```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

## Constraints

- 1 <= preorder.length <= 3000
- inorder.length == preorder.length
- -3000 <= preorder[i], inorder[i] <= 3000
- preorder and inorder consist of unique values.
- Each value of inorder also appears in preorder.
- preorder is guaranteed to be the preorder traversal of the tree.
- inorder is guaranteed to be the inorder traversal of the tree.

## Approach

The solution uses a recursive approach based on the properties of preorder and inorder traversals:

### Key Insights:
1. **Preorder traversal**: Root → Left subtree → Right subtree
2. **Inorder traversal**: Left subtree → Root → Right subtree
3. The first element in preorder is always the root
4. In inorder, all elements before the root belong to the left subtree, and all elements after the root belong to the right subtree

### Algorithm:
1. Use the first element of preorder as the root
2. Find the root's position in inorder array
3. Recursively construct left subtree using elements before root in inorder
4. Recursively construct right subtree using elements after root in inorder
5. Update preorder indices accordingly

### Time Complexity: O(n²)
- For each node, we search for its position in inorder array: O(n)
- We do this for n nodes: O(n²)

### Space Complexity: O(n)
- Recursion stack depth can be at most n (height of tree)
- Additional space for slicing arrays: O(n)

## Alternative Approach
This can also be solved using a stack-based approach, which is more intuitive and can achieve O(n) time complexity with proper optimization.
