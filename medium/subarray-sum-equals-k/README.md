# 560. Subarray Sum Equals K

**Difficulty:** Medium

## Problem Description
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

### Example 1
```
Input: nums = [1,1,1], k = 2
Output: 2
```

### Example 2
```
Input: nums = [1,2,3], k = 3
Output: 2
```

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Approach
We can solve this efficiently using a **prefix sum + hash map** technique.

Idea:
- Let `currSum` be the running prefix sum of the array.
- A subarray `nums[l..r]` has sum `k` if and only if:
  - `prefixSum[r] - prefixSum[l-1] = k`, i.e. `prefixSum[l-1] = prefixSum[r] - k`.
- As we iterate through `nums`, for each position we want to know how many times we've seen a prefix sum equal to `currSum - k` before. Each such occurrence corresponds to a subarray ending at the current index with sum `k`.

Algorithm:
1. Initialize:
   - `result = 0` (count of subarrays),
   - `currSum = 0`,
   - `prefixSum = {0: 1}` as a dictionary mapping prefix sum to its frequency (base case: sum 0 seen once).
2. For each element `n` in `nums`:
   - Update `currSum += n`.
   - Compute `diff = currSum - k`.
   - If `diff` exists in `prefixSum`, increment `result` by `prefixSum[diff]`.
   - Update `prefixSum[currSum] = prefixSum.get(currSum, 0) + 1`.
3. Return `result`.

This counts all subarrays ending at each index that sum to `k`.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(nums)`, since we make a single pass through the array.
- **Space Complexity:** `O(n)` in the worst case for the `prefixSum` dictionary.

