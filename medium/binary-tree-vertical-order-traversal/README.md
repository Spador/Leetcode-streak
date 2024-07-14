# Binary Tree Vertical Order Traversal

Return the vertical order traversal of a binary tree's nodes' values.

## Approach
- Use BFS with column tracking
- Track minimum and maximum column values
- Store nodes in a dictionary by column
- Process nodes level by level
- Return values ordered by column

Time Complexity: O(n)
Space Complexity: O(n) 