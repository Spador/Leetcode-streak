# spador

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minheap = []
        result = {}
        i = 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(minheap, (end - start + 1, end))
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            result[q] = minheap[0][0] if minheap else -1

        return [result[q] for q in queries]
