from typing import List
import collections
import heapq

# spador

# Time complexity: O(ElogV)

class Solution:

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges = collections.defaultdict(list)

        for u, v, w in times:

            edges[u].append((v, w))
        
        
        minHeap = [(0, k)]

        visit = set()

        finalTime = 0



        while minHeap:

            w1, v1 = heapq.heappop(minHeap)

            if v1 in visit:

                continue

            visit.add(v1)

            finalTime = max(finalTime, w1)



            for v2, w2 in edges[v1]:

                heapq.heappush(minHeap, (w1 + w2, v2))
        
        
        return finalTime if len(visit) == n else -1
