# 57. Insert Interval

**Difficulty:** Medium

## Problem Description
You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [start_i, end_i]` represent the start and the end of the `i`th interval and `intervals` is sorted in ascending order by `start_i`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `start_i` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.

Note that you don't need to modify `intervals` in-place. You can make a new array and return it.

## Examples

### Example 1
```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

### Example 2
```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```

## Constraints
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Approach
We can insert and merge in a single pass over the existing intervals.

Given that `intervals` is already sorted and non-overlapping:
1. Initialize an empty result list `result`.
2. Iterate over each interval `intervals[i]`:
   - **Case 1: new interval ends before the current interval starts**  
     - If `newInterval[1] < intervals[i][0]`, then `newInterval` does not overlap with this and any following interval (because of sorting).  
       - Append `newInterval` to `result`.  
       - Return `result + intervals[i:]` (append the rest unchanged).
   - **Case 2: new interval starts after the current interval ends**  
     - If `newInterval[0] > intervals[i][1]`, then `intervals[i]` is completely before `newInterval`.  
       - Append `intervals[i]` to `result`.
   - **Case 3: Overlap**  
     - Otherwise, the intervals overlap, so merge them by updating `newInterval` to:
       - `newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]`.
3. After processing all intervals, append the (possibly merged) `newInterval` to `result`.
4. Return `result`.

This logic ensures we maintain sorted, non-overlapping intervals while inserting and merging as needed.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(intervals)`, since we scan the list once.
- **Space Complexity:** `O(n)` for the output list.

