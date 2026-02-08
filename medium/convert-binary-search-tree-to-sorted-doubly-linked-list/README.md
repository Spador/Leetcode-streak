# 426. Convert Binary Search Tree to Sorted Doubly Linked List

**Difficulty:** Medium

## Problem Description
Convert a Binary Search Tree (BST) to a sorted **circular doubly-linked list** in place.

You can think of the `left` and `right` pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list:
- The predecessor of the first element is the last element.
- The successor of the last element is the first element.

We want to do the transformation **in place**. After the transformation, the `left` pointer of the tree node should point to its predecessor, and the `right` pointer should point to its successor. You should return the pointer to the smallest element of the linked list.

## Examples

### Example 1
```
Input: root = [4,2,5,1,3]
Output: [1,2,3,4,5]
```

### Example 2
```
Input: root = [2,1,3]
Output: [1,2,3]
```

## Constraints
- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`.
- All the values of the tree are unique.

## Approach
We use an **in-order traversal** of the BST to visit nodes in sorted order and link them into a doubly-linked list as we go.

1. If the tree is empty, return `None`.
2. Maintain two pointers in the `Solution` object:
   - `self.first` – pointer to the smallest (leftmost) node in the BST.
   - `self.last` – pointer to the previously visited node during in-order traversal.
3. Perform an in-order DFS:
   - Traverse the left subtree.
   - At the current node:
     - If `self.last` is `None`, this is the first (smallest) node; set `self.first = node`.
     - Otherwise, link the current node with `self.last`:
       - `node.left = self.last`
       - `self.last.right = node`
     - Update `self.last = node`.
   - Traverse the right subtree.
4. After the traversal, link the head and tail to make the list circular:
   - `self.first.left = self.last`
   - `self.last.right = self.first`
5. Return `self.first`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n` is the number of nodes, since we visit each node once.
- **Space Complexity:** `O(1)` extra space (excluding the recursion stack, which is `O(h)` where `h` is the tree height).
