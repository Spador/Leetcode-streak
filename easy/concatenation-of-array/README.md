# 1929. Concatenation of Array

**Difficulty:** Easy

## Problem Description
Given an integer array `nums` of length `n`, you want to create an array `ans` of length `2n` where:

- `ans[i] == nums[i]` and
- `ans[i + n] == nums[i]` for `0 <= i < n` (0-indexed).

Specifically, `ans` is the concatenation of two `nums` arrays.

Return the array `ans`.

## Examples

### Example 1
```
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```

### Example 2
```
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
```

## Constraints
- `n == nums.length`
- `1 <= n <= 1000`
- `1 <= nums[i] <= 1000`

## Approach
We can construct the result in a single pass with `O(1)` extra space (besides the output array):

1. Let `n = len(nums)`.
2. Initialize `ans` as an array of size `2 * n`.
3. For each index `i` and value `num` in `nums`:
   - Set `ans[i] = num`.
   - Set `ans[i + n] = num`.
4. Return `ans`.

This directly follows the definition of the problem.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n = len(nums)`.
- **Space Complexity:** `O(n)` for the output array `ans`.
