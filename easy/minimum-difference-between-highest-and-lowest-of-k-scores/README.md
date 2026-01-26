# 1984. Minimum Difference Between Highest and Lowest of K Scores

**Difficulty:** Easy

## Problem Description
You are given a 0-indexed integer array `nums`, where `nums[i]` represents the score of the `ith` student. You are also given an integer `k`.

Pick the scores of any `k` students from the array so that the difference between the highest and the lowest of the `k` scores is minimized.

Return the minimum possible difference.

## Examples

### Example 1
```
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
```

### Example 2
```
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
```

## Constraints
- `1 <= k <= nums.length <= 1000`
- `0 <= nums[i] <= 10^5`

## Approach
1. Sort the array in ascending order.
2. Use a sliding window of size `k` to find the minimum difference.
3. For each window of `k` consecutive elements, calculate the difference between the maximum (last element) and minimum (first element) in that window.
4. Track the minimum difference across all windows.

## Algorithm
- Handle edge cases: if `len(nums)` is 0 or 1, return `0`.
- Sort the array `nums`.
- Initialize `res = float("inf")`.
- Iterate through all possible windows of size `k`:
  - For `i` from `0` to `len(nums) - k`:
    - Calculate the difference: `nums[i + k - 1] - nums[i]` (difference between the last and first element in the window).
    - Update `res = min(res, nums[i + k - 1] - nums[i])`.
- Return `res`.

## Time & Space Complexity
- **Time Complexity:** `O(n log n)` where `n = len(nums)`. Sorting takes `O(n log n)` and the sliding window iteration takes `O(n)`.
- **Space Complexity:** `O(1)` if we don't count the space used for sorting (in-place sort), or `O(n)` if sorting requires additional space.
