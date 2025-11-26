# 416. Partition Equal Subset Sum

**Difficulty:** Medium

## Problem Description
Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `false` otherwise.

## Examples

### Example 1
```
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

### Example 2
```
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
```

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`

## Approach
1. This is a variation of the subset sum problem, which can be solved using dynamic programming.
2. First, check if the total sum is even. If not, return `false` immediately (cannot partition odd sum into two equal parts).
3. The target sum for each subset is `total_sum / 2`.
4. Use a set-based DP approach to track all possible sums that can be achieved.
5. Iterate backwards through the array, and for each number, update the set of achievable sums by adding the current number to all existing sums.
6. If at any point we achieve the target sum, return `true` immediately.
7. After processing all numbers, if the target sum was never achieved, return `false`.

## Algorithm
- Calculate `target = sum(nums) // 2`. If `sum(nums) % 2 != 0`, return `false`.
- Initialize a set `dp = {0}` representing achievable sums (starting with sum 0).
- For each number `nums[i]` from the end to the beginning:
  - Create a temporary set `tempdp`.
  - For each sum `n` in the current `dp`:
    - If `nums[i] + n == target`, return `true` (found valid partition).
    - Add `nums[i] + n` and `n` to `tempdp` (include or exclude current number).
  - Update `dp = tempdp`.
- Return `false` if target was never reached.

## Time & Space Complexity
- **Time Complexity:** `O(n * sum)` where `n` is the array length and `sum` is the total sum. In worst case, the set can contain up to `sum` distinct values.
- **Space Complexity:** `O(sum)` for the set storing achievable sums.
