# Matrix Similarity After Cyclic Shifts

Return true if the matrix after k cyclic shifts (even rows left, odd rows right) is identical to the original.

## Approach
- Reduce k to k % cols; if 0 the matrix is always unchanged
- For each row check if every element equals the element at the shifted position
- Even rows shift left by `shift`, so check row[c] == row[(c + shift) % cols]
- Odd rows shift right by `shift`, so check row[c] == row[(c + cols - shift) % cols]

Time Complexity: O(m * n)
Space Complexity: O(1)
