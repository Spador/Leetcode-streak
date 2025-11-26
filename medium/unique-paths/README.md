# 62. Unique Paths

**Difficulty:** Medium

## Problem Description
There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

## Examples

### Example 1
```
Input: m = 3, n = 7
Output: 28
```

### Example 2
```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## Constraints
- `1 <= m, n <= 100`

## Approach
1. This is a classic dynamic programming problem that can be solved with space optimization.
2. The number of paths to reach any cell `(i, j)` equals the sum of paths from `(i-1, j)` (above) and `(i, j-1)` (left).
3. Use a space-optimized approach: maintain only one row at a time instead of the entire grid.
4. Initialize the bottom row with all `1`s (only one way to reach any cell in the last row by moving right).
5. For each row above, compute the new row by working backwards: `newRow[j] = newRow[j+1] + row[j]` (right + down).
6. The first element of the final row contains the answer.

## Algorithm
- Initialize `row = [1] * n` (bottom row, all cells have 1 path).
- For each row `i` from `m-2` down to `0`:
  - Create `newRow = [1] * n` (rightmost column always has 1 path).
  - For each column `j` from `n-2` down to `0`:
    - `newRow[j] = newRow[j+1] + row[j]` (paths from right + paths from below).
  - Update `row = newRow`.
- Return `row[0]` (top-left corner).

## Time & Space Complexity
- **Time Complexity:** `O(m * n)` - we iterate through each cell once.
- **Space Complexity:** `O(n)` - we only maintain one row at a time instead of the full `m x n` grid.
