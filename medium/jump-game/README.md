# 55. Jump Game

**Difficulty:** Medium

## Problem Description
You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

## Examples

### Example 1
```
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

### Example 2
```
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Approach
There is a dynamic programming solution, but a greedy approach achieves `O(n)` time and `O(1)` space.

Key idea:
- Track the **leftmost index** (`goal`) from which we know we can reach the end.
- Initialize `goal` as the last index (`len(nums) - 1`).
- Traverse the array **backwards**:
  - At each index `i`, if `i + nums[i] >= goal`, it means we can jump from `i` to `goal` (or beyond), so we update `goal = i`.
- At the end, if `goal == 0`, it means we can reach the last index starting from index `0`.

## Algorithm
- Set `goal = len(nums) - 1`.
- For `i` from `len(nums) - 1` down to `0`:
  - If `i + nums[i] >= goal`, set `goal = i`.
- After the loop, return `True` if `goal == 0`, otherwise `False`.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(nums)`, because we traverse the array once from right to left.
- **Space Complexity:** `O(1)`, since we only use a few variables.

