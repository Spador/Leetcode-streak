# 827. Making A Large Island

Return the size of the largest island after changing at most one 0 to 1 in an n x n binary grid.

## Approach
- DFS to label each island with a unique integer ID (starting from 2) and record its area in a map
- For each 0 cell, simulate flipping it by summing the areas of all uniquely-labeled neighboring islands plus 1
- Track the maximum area across all 0 cells; initialize max to the largest pre-existing island

Time Complexity: O(n^2)
Space Complexity: O(n^2)
