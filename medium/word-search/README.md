# 79. Word Search

## Problem Description

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Examples

### Example 1:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

### Example 2:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

### Example 3:
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Constraints

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- board and word consists of only lowercase and uppercase English letters.

## Approach

- Use DFS with backtracking to search for the word in the grid
- Start from each cell in the grid and recursively explore all 4 directions (up, down, left, right)
- Mark visited cells temporarily with '#' to avoid revisiting the same cell in the current path
- If the current path doesn't lead to a solution, backtrack by restoring the original character
- Handle edge case for 1x1 grid where the only cell must match the word

## Time and Space Complexity

- **Time Complexity**: O(m * n * 4^L) where m and n are grid dimensions and L is the length of the word
  - We start from each cell (m * n possibilities)
  - From each cell, we can go in 4 directions
  - In the worst case, we explore paths up to length L
- **Space Complexity**: O(L) for the recursion stack depth (maximum depth is the length of the word)

## Follow up
Could you use search pruning to make your solution faster with a larger board?

## Difficulty
Medium
