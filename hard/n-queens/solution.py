class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 2 or n == 3:
            return []

        
        col = set()
        posDiag = set()  # this will always follow pattern (row + col)
        negDiag = set()  # this will always follow pattern (row - col)

        result = []
        board = [["."] * n for _ in range(n)]

        def backTrack(r):
            if r == n:
                result.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backTrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
            
        backTrack(0)
        return result
