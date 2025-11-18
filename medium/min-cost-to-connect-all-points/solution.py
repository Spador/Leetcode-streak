from typing import List
import heapq

# spador

# Cost to make a MST(Minimum Spanning Tree)

class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        
        # make adjacency list for a fully connected graph with node->[Manhatten Distance, node]
        adj = {i:[] for i in range(n)}


        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                Mandist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([Mandist, j])
                adj[j].append([Mandist, i])


        # Prim's Algorithm
        result = 0
        visit = set()
        minHeap = [[0, 0]] # min heap with starting node
        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            result += cost
            visit.add(i)
            for dist, neibhour in adj[i]:
                if neibhour not in visit:
                    heapq.heappush(minHeap, [dist, neibhour])
        return result
