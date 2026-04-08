# spador

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direc = 0
        x, y = 0, 0
        result = 0

        obstacle = {tuple(o) for o in obstacles}

        for c in commands:
            if c == -1:
                direc = (direc + 1) % 4
            elif c == -2:
                direc = (direc - 1) % 4
            else:
                dx, dy = direction[direc]

                for _ in range(c):
                    if (x + dx, y + dy) not in obstacle:
                        x += dx
                        y += dy
                    else:
                        break

                    result = max(result, x**2 + y**2)
        return result
