# 213. House Robber II

**Difficulty:** Medium

## Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Examples

### Example 1
```
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

### Example 2
```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

### Example 3
```
Input: nums = [1,2,3]
Output: 3
```

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## Approach
1. This is an extension of House Robber I, but with houses arranged in a circle.
2. The key constraint is that the first and last houses are adjacent, so we cannot rob both.
3. Break the circular constraint by considering two cases:
   - Case 1: Rob houses from index 1 to n-1 (exclude first house).
   - Case 2: Rob houses from index 0 to n-2 (exclude last house).
   - Case 3: If only one house, just return that value.
4. Use the same helper function from House Robber I to solve each linear subproblem.
5. Return the maximum of all three cases.

## Algorithm
- If the array has only one element, return `nums[0]`.
- Create a helper function that solves the linear House Robber problem (same as House Robber I).
- Consider three scenarios:
  - Rob only the first house: `nums[0]` (if we take first, we can't take last).
  - Rob houses from index 1 to end: `helper(nums[1:])` (exclude first house).
  - Rob houses from index 0 to second-to-last: `helper(nums[:-1])` (exclude last house).
- Return the maximum of these three cases.

## Time & Space Complexity
- **Time Complexity:** `O(n)` - we solve two linear subproblems, each taking O(n) time.
- **Space Complexity:** `O(1)` - the helper function uses only two variables, and we create two subarrays which are O(n) space, but this is input-dependent.
