# Maximum Width of Binary Tree

Return the maximum width of a binary tree, counting null nodes between end-nodes at each level.

## Approach
- BFS with each node assigned a heap-style index (root = 1, left child = 2*i, right child = 2*i + 1)
- Track the index of the first node seen at each new level
- Width at each level = current node index - first index at that level + 1
- Take the max across all levels

Time Complexity: O(n)
Space Complexity: O(n)
