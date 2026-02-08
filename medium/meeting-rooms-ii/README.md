# 253. Meeting Rooms II

**Difficulty:** Medium

## Problem Description
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

## Examples

### Example 1
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

### Example 2
```
Input: intervals = [[7,10],[2,4]]
Output: 1
```

## Constraints
- `1 <= intervals.length <= 10^4`
- `0 <= start_i < end_i <= 10^6`

## Approach
We can think of this as tracking how many meetings overlap at any point in time. A common solution uses a **min-heap** of end times:

1. Sort the intervals by their start time.
2. Maintain a min-heap `minheap` that stores the end times of meetings currently using a room.
3. For each interval `[start, end]` in the sorted list:
   - While there is at least one meeting in the heap whose end time is less than or equal to `start`, pop it from the heap (that room is now free).
   - Push the current meeting's `end` time onto the heap (this meeting needs a room).
   - Track `max_rooms` as the maximum size of the heap seen so far.
4. The answer is `max_rooms`, which represents the maximum number of rooms simultaneously in use.

## Time & Space Complexity
- **Time Complexity:** `O(n log n)` due to sorting and heap operations, where `n = len(intervals)`.
- **Space Complexity:** `O(n)` in the worst case for the heap.
