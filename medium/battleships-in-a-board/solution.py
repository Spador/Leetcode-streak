# spador
# Time: O(M*N)
# Space: O(1)


# Iterating through the entire board cell by cell from (0,0) to (m,n).
# Just checking if the (n-1,m) left cell or (n,m-1) up cell has "X". if yes then don't increment the count.

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        result = 0

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    # check for horizontal boat
                    if i > 0 and board[i - 1][j] == "X":
                        continue
                    # check for vertical boat
                    elif j > 0 and board[i][j - 1] == "X":
                        continue
                    else:
                        result += 1
        return result

