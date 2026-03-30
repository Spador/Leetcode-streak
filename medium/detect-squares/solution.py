#spador

class DetectSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[(point[0], point[1])] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        result = 0
        x1, y1 = point
        for x2, y2 in self.points:
            if (abs(x1 - x2) != abs(y1 - y2)) or (x1 == x2 and y1 == y2):
                continue
            result += (self.pointsCount[(x1, y2)] * self.pointsCount[(x2, y1)])
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
