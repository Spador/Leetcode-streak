# 419. Battleships in a Board

**Difficulty:** Medium

## Problem Description
Given an `m x n` matrix `board` where each cell is a battleship `'X'` or empty `'.'`, return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on `board`. In other words, they can only be made of the shape `1 x k` (1 row, k columns) or `k x 1` (k rows, 1 column), where `k` can be of any size. At least one horizontal or vertical cell separates two battleships (i.e., there are no adjacent battleships).

## Examples

### Example 1
```
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
```

### Example 2
```
Input: board = [["."]]
Output: 0
```

## Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is either `'.'` or `'X'`.

## Follow up
Could you do it in one-pass, using only `O(1)` extra memory and without modifying the values `board`?

## Approach
We can solve this in one pass with `O(1)` extra space by **counting only the starting cells of each battleship**.

Key idea:
- Each battleship is a contiguous line of `'X'` cells either horizontally or vertically.
- If we scan each cell `(i, j)`:
  - Whenever we see an `'X'`, we only want to count it if it is the **top-left** cell of a ship.
  - That means there should be **no `'X'` directly above** it and **no `'X'` directly to its left`**.

Algorithm:
1. Initialize `result = 0`.
2. For each cell `(i, j)` in the board:
   - If `board[i][j] != 'X'`, skip.
   - If `i > 0` and `board[i - 1][j] == 'X'`, skip (this cell is part of a vertical ship that started above).
   - Else if `j > 0` and `board[i][j - 1] == 'X'`, skip (this cell is part of a horizontal ship that started to the left).
   - Otherwise, this is the first cell of a new ship, so increment `result`.
3. Return `result`.

This respects the follow-up: one pass, constant extra memory, and no modification of `board`.

## Time & Space Complexity
- **Time Complexity:** `O(m * n)`, where `m` and `n` are the dimensions of the board; we visit each cell once.
- **Space Complexity:** `O(1)` extra space.

