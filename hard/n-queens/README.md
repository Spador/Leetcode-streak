# 51. N-Queens

**Difficulty:** Hard

## Problem Description

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

## Examples

### Example 1:
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

### Example 2:
```
Input: n = 1
Output: [["Q"]]
```

## Constraints

- 1 <= n <= 9

## Approach

This is a classic backtracking problem that requires:

1. **Backtracking Strategy**: Try placing queens row by row, ensuring no conflicts.
2. **Efficient Conflict Detection**: Use sets to track occupied columns and diagonals for O(1) conflict checking:
   - `col` set: tracks occupied columns
   - `posDiag` set: tracks positive diagonals (row + col pattern)
   - `negDiag` set: tracks negative diagonals (row - col pattern)
3. **Base Case**: When all n queens are placed successfully, add the board configuration to results.
4. **Recursive Case**: For each row, try placing a queen in each column and recursively solve for the next row.

## Algorithm

1. Handle edge cases: n=2 and n=3 have no solutions, return empty list
2. Initialize tracking sets for columns and diagonals
3. Create empty board and result list
4. For each row from 0 to n-1:
   - Try placing a queen in each column of the current row
   - Check conflicts using sets (O(1) time)
   - If no conflicts, place queen, update tracking sets, and recurse
   - Backtrack by removing queen and cleaning up tracking sets
5. When all queens are placed, add board configuration to results

## Key Optimizations

- **Diagonal Tracking**: Use mathematical patterns to identify diagonals:
  - Positive diagonal: `row + col` (constant sum)
  - Negative diagonal: `row - col` (constant difference)
- **Set-based Conflict Detection**: O(1) time complexity for conflict checking
- **Early Termination**: Skip impossible cases (n=2, n=3) immediately

## Time Complexity

- **Time**: O(N!) where N is the board size
  - In the worst case, we explore all possible queen placements
  - Each placement involves O(1) conflict checking using sets
- **Space**: O(N) for the recursion stack, tracking sets, and board representation

## Solution

The solution uses optimized backtracking with set-based conflict detection:
- Tracks occupied columns, positive diagonals, and negative diagonals using sets
- Uses mathematical patterns to identify diagonal conflicts efficiently
- Implements proper backtracking with cleanup of tracking data structures
