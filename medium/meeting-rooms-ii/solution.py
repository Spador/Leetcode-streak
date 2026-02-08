# spador

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])

        max_rooms = 0
        minheap = []

        for start, end in intervals:
            while minheap and start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, end)
            max_rooms = max(max_rooms, len(minheap))
        return max_rooms

# Time: O(nlogn) => time to sort 
# Space: O(n) => space for the heap
