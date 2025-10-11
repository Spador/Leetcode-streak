# spador

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)

        if m == 1 and n == 1:
            return board[0][0] == word
        
        def backTrack(pos, index):
            i, j = pos

            if index == w:
                return True
            
            if board[i][j] != word[index]:
                return False

            char = board[i][j]
            board[i][j] = '#'       # to mark it visited

            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = i + x, j + y
                if 0 <= r < m and 0 <= c < n:
                    if backTrack((r,c), index + 1):
                        return True
            board[i][j] = char
            return False


        for i in range(m):
            for j in range(n):
                if backTrack((i, j), 0):
                    return True
        return False
