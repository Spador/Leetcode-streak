# Surrounded Regions

Given an m x n board of 'X' and 'O', capture all regions of 'O' fully surrounded by 'X' by replacing them with 'X' in-place.

## Approach
- Phase 1: DFS from every 'O' on the border, marking reachable cells as 'Q' (safe, cannot be captured)
- Phase 2: Convert all remaining 'O' to 'X' (these are fully surrounded)
- Phase 3: Convert all 'Q' back to 'O' (restore the safe border-connected cells)

Time Complexity: O(m * n)
Space Complexity: O(m * n)
