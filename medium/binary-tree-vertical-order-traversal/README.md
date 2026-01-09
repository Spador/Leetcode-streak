# Binary Tree Vertical Order Traversal

Return the vertical order traversal of a binary tree's nodes' values.

## Approach 1 (BFS with column tracking)
- Use BFS with column tracking
- Track minimum and maximum column values
- Store nodes in a dictionary by column
- Process nodes level by level (top to bottom, left to right within the same column)
- Return values ordered by column from `minCol` to `maxCol`

Time Complexity: O(n)  
Space Complexity: O(n)

## Approach 2 (Alternative BFS implementation)
- Use a queue of `(node, col)` pairs starting from `(root, 0)`.
- Maintain `minCol` and `maxCol` while traversing to know the column range.
- Use a `defaultdict(list)` to collect node values for each column index.
- For each node:
  - Append its value to `colMap[col]`.
  - Enqueue its left child with `col - 1` and right child with `col + 1` if they exist.
- After BFS, build the result list using columns from `minCol` to `maxCol` in order.

This approach matches the BFS-based solution variant added in `solution2.py`. 