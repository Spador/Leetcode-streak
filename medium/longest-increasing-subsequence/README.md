# 300. Longest Increasing Subsequence

**Difficulty:** Medium

## Problem Description
Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

## Examples

### Example 1
```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

### Example 2
```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

### Example 3
```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## Constraints
- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Follow up
Can you come up with an algorithm that runs in `O(n log(n))` time complexity?

## Approach
1. Use dynamic programming with a bottom-up approach.
2. For each position `i`, `dp[i]` represents the length of the longest increasing subsequence starting at index `i`.
3. Initialize all `dp[i] = 1` (each element is a subsequence of length 1).
4. Iterate backwards through the array. For each element at index `i`, check all elements `j` that come after it.
5. If `nums[i] < nums[j]`, we can extend the subsequence starting at `j` by including `i`, so update `dp[i] = max(dp[i], 1 + dp[j])`.
6. Return the maximum value in the `dp` array.

## Algorithm
- Initialize `dp` array of size `len(nums)` with all values set to `1`.
- For `i` from `len(nums) - 1` down to `0`:
  - For `j` from `i + 1` to `len(nums) - 1`:
    - If `nums[i] < nums[j]`, update `dp[i] = max(dp[i], 1 + dp[j])`.
- Return `max(dp)`.

## Time & Space Complexity
- **Time Complexity:** `O(n²)` - nested loops where we check each element against all subsequent elements.
- **Space Complexity:** `O(n)` - for the DP array.

## Note
There is a better solution with `O(n log n)` time complexity using binary search and maintaining a tails array, but this solution uses the more intuitive `O(n²)` DP approach.
