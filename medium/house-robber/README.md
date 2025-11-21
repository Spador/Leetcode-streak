# 198. House Robber

**Difficulty:** Medium

## Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Examples

### Example 1
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

### Example 2
```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Approach
1. This is a classic dynamic programming problem where we need to maximize the sum while avoiding adjacent elements.
2. For each house, we have two choices: rob it or skip it.
3. If we rob the current house, we cannot rob the previous house. If we skip the current house, we can use the maximum from the previous house.
4. Use two variables `rob1` and `rob2` to track the maximum money robbed up to two positions back.
5. For each house, calculate the maximum between robbing the current house plus `rob1` (two houses back) or keeping `rob2` (one house back).
6. Update `rob1` to `rob2` and `rob2` to the new maximum, effectively sliding the window forward.

## Algorithm
- Initialize `rob1 = 0` (two houses back) and `rob2 = 0` (one house back).
- For each house `n` in `nums`:
  - Calculate `temp = max(rob1 + n, rob2)` (rob current house + two houses back, or skip and keep one house back).
  - Update `rob1 = rob2` and `rob2 = temp` (slide the window forward).
- Return `rob2` as the maximum amount that can be robbed.

## Time & Space Complexity
- **Time Complexity:** `O(n)` - single pass through the array.
- **Space Complexity:** `O(1)` - only using two variables regardless of input size.
