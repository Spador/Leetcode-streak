# 1200. Minimum Absolute Difference

**Difficulty:** Easy

## Problem Description
Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order (with respect to pairs), each pair `[a, b]` follows:

- `a`, `b` are from `arr`
- `a < b`
- `b - a` equals to the minimum absolute difference of any two elements in `arr`

## Examples

### Example 1
```
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
```

### Example 2
```
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
```

### Example 3
```
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
```

## Constraints
- `2 <= arr.length <= 10^5`
- `-10^6 <= arr[i] <= 10^6`

## Approach
1. Since we need the minimum absolute difference between any two elements, it is natural to **sort** the array first.
2. After sorting, the minimum absolute difference must occur between **adjacent elements** in the sorted array (because any pair that is not adjacent will have a difference at least as large as some adjacent pair in between).
3. Make one pass over the sorted array to compute the global minimum difference between consecutive elements.
4. Make another pass to collect all adjacent pairs whose difference equals this minimum difference.

## Algorithm
- Sort `arr` in non-decreasing order.
- Initialize `currMin` as the difference between the first and last elements (or simply a large number).
- First loop:
  - For each `i` from `0` to `len(arr) - 2`:
    - Update `currMin = min(currMin, arr[i+1] - arr[i])`.
- Second loop:
  - Initialize an empty result list `result`.
  - For each `i` from `0` to `len(arr) - 2`:
    - If `arr[i+1] - arr[i] == currMin`, append `[arr[i], arr[i+1]]` to `result`.
- Return `result`.

## Time & Space Complexity
- **Time Complexity:** `O(n log n)` due to sorting, where `n = len(arr)`. The subsequent linear scans are `O(n)`.
- **Space Complexity:** `O(1)` additional space (ignoring the output list), since sorting can be done in-place and we only use a few extra variables.

