import heapq
from typing import List


class MedianFinder:

    def __init__(self):
        # Two heaps: small is a max-heap (via negatives), large is a min-heap
        self.small = []  # max-heap (store negatives)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # Push to max-heap (small) first
        heapq.heappush(self.small, -num)

        # Ensure every element in large is >= every element in small
        if self.small and self.large and (-self.small[0] > self.large[0]):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Rebalance sizes so that their lengths differ by at most 1
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)
        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return ((-self.small[0]) + self.large[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
