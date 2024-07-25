# 287. Find the Duplicate Number

## Problem Description

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is only one repeated number in `nums`, return this repeated number.

You must solve the problem without modifying the array `nums` and using only constant extra space.

## Examples

### Example 1:
```
Input: nums = [1,3,4,2,2]
Output: 2
```

### Example 2:
```
Input: nums = [3,1,3,4,2]
Output: 3
```

### Example 3:
```
Input: nums = [3,3,3,3,3]
Output: 3
```

## Constraints

- `1 <= n <= 10^5`
- `nums.length == n + 1`
- `1 <= nums[i] <= n`
- All the integers in `nums` appear only once except for precisely one integer which appears two or more times.

## Follow up

- How can we prove that at least one duplicate number must exist in nums?
- Can you solve the problem in linear runtime complexity?

## Approach

The solution uses **Floyd's Cycle Detection Algorithm (Tortoise and Hare)**:

1. **Phase 1 - Find Intersection**: Use two pointers (slow and fast) to find where they meet in the cycle
2. **Phase 2 - Find Entrance**: Reset one pointer to the start and move both pointers one step at a time until they meet
3. **Return Result**: The meeting point is the duplicate number

**Key Insight**: Treat the array as a linked list where each value points to the index of that value. The duplicate creates a cycle, and the entrance of the cycle is the duplicate number.

**Why it works**: 
- The duplicate number creates a cycle in the "linked list" representation
- Floyd's algorithm finds the entrance of the cycle, which is the duplicate

## Time Complexity

O(n) - Linear time complexity.

## Space Complexity

O(1) - Only using two pointers regardless of input size.
