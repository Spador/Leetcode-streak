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
2. **Conflict Detection**: Check if a queen can be placed without attacking other queens:
   - No queen in the same column
   - No queen in the same diagonal (both main and anti-diagonal)
3. **Base Case**: When all n queens are placed successfully, add the board configuration to results.
4. **Recursive Case**: For each row, try placing a queen in each column and recursively solve for the next row.

## Algorithm

1. Start with an empty board
2. For each row from 0 to n-1:
   - Try placing a queen in each column of the current row
   - Check if the placement is valid (no conflicts)
   - If valid, place the queen and recursively solve for the next row
   - Backtrack by removing the queen and trying the next column
3. When all queens are placed, add the board configuration to results

## Time Complexity

- **Time**: O(N!) where N is the board size
  - In the worst case, we explore all possible queen placements
  - Each placement involves checking conflicts which takes O(N) time
- **Space**: O(N) for the recursion stack and board representation

## Note

This problem is a classic example of backtracking and constraint satisfaction. The solution will be implemented using recursive backtracking with proper conflict detection.
