# 973. K Closest Points to Origin

## Problem Description

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Examples

### Example 1:
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
```

### Example 2:
```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
```

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`

## Approach

- Calculate the squared distance from each point to the origin (x² + y²)
- Since we only need to compare distances, we can avoid computing the square root
- Transform each point into [distance, x, y] format for heap operations
- Use a min-heap to efficiently get the k closest points
- Extract the k smallest distances from the heap
- Return the points in the original [x, y] format

## Time and Space Complexity

- **Time Complexity**: O(n log k) where n is the number of points
  - O(n) to calculate distances and transform points
  - O(n log n) for heapify operation
  - O(k log n) for extracting k elements from heap
  - Overall: O(n log n)
- **Space Complexity**: O(1) extra space (not counting the input array)
  - We modify the input array in-place

## Difficulty
Medium
