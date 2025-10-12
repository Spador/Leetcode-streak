# spador

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = x**2 + y**2
            points[i] = [dist, x, y]
        result = []
        heapq.heapify(points)
        for i in range(k):
            dist, x, y = heapq.heappop(points)
            result.append([x,y])
        return result
        
