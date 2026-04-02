# spador

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] != 'O':
                return
            board[r][c] = 'Q'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)


        # phase 1: run dfs on all the border cell and mark them (O -> Q)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r, c)

        # phase 2: run a nested loop to change remaining to X (O -> X)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        # phase 3: run a nested loop to change Q to O (Q -> o)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Q":
                    board[r][c] = "O"
