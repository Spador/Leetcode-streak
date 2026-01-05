# 45. Jump Game II

**Difficulty:** Medium

## Problem Description
You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at index `0`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at index `i`, you can jump to any index `i + j` where:

- `0 <= j <= nums[i]` and
- `i + j < n`

Return the minimum number of jumps to reach index `n - 1`. The test cases are generated such that you can reach index `n - 1`.

## Examples

### Example 1
```
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. 
Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2
```
Input: nums = [2,3,0,1,4]
Output: 2
```

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

## Approach
We can solve this problem optimally using a **greedy** approach in `O(n)` time.

Idea:
- We want to find the minimum number of jumps to reach the last index.
- Think of it as expanding a "window" of indices that are reachable with the current number of jumps.
- For each layer of reachable indices, we compute how far we can reach with one more jump.

Steps:
1. Maintain two pointers, `left` and `right`, representing the current range of indices we can reach with the current number of jumps.
2. Initialize `result = 0`, `left = 0`, `right = 0`.
3. While `right < len(nums) - 1`:
   - Compute the farthest index `far` we can reach from any index in the current window `[left, right]`:
     - For each `i` in `[left, right]`, update `far = max(far, i + nums[i])`.
   - Move the window to the next layer:
     - Set `left = right + 1`, `right = far`.
   - Increment `result` (we used one more jump).
4. When the loop ends, `result` will be the minimum number of jumps needed to reach the last index.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(nums)`, since each index is processed at most once within the window expansions.
- **Space Complexity:** `O(1)`, as we use only a few variables.

