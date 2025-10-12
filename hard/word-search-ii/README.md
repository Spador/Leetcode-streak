# 212. Word Search II

## Problem Description

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Examples

### Example 1:
```
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

### Example 2:
```
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

## Constraints

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 12`
- `board[i][j]` is a lowercase English letter.
- `1 <= words.length <= 3 * 10^4`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- All the strings of words are unique.

## Approach

- Use a Trie (Prefix Tree) to store all the words for efficient searching
- Build the Trie by adding each word from the input list
- Use DFS with backtracking to traverse the board starting from each cell
- For each cell, check if the character exists in the current Trie node's children
- If a word is found (node.isWord = True), add it to the result set
- Use a visit set to track visited cells in the current path to avoid revisiting
- Remove cells from visit set when backtracking
- Return all unique words found as a list

## Time and Space Complexity

- **Time Complexity**: O(m * n * 4^L + W * L) where:
  - m, n are board dimensions
  - L is the maximum word length
  - W is the number of words
  - O(W * L) for building the Trie
  - O(m * n * 4^L) for DFS traversal in worst case
- **Space Complexity**: O(W * L + L) where:
  - O(W * L) for the Trie storage
  - O(L) for the recursion stack and visit set

## Difficulty
Hard
