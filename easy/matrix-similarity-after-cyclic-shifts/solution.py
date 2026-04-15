# spador

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        cols = len(mat[0])
        shift = k % cols
        if shift == 0:
            return True

        for i, row in enumerate(mat):
            for c in range(cols):
                if i % 2 == 0:      # even rows
                    if row[c] != row[(c + shift) % cols]:
                        return False
                else:               # odd rows
                    if row[c] != row[(c + cols - shift) % cols]:
                        return False
        return True
