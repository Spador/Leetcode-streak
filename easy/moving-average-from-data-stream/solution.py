# spador

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.movingSum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.movingSum += val
        if len(self.queue) > self.size:
            self.movingSum -= self.queue.popleft()
        return self.movingSum / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
