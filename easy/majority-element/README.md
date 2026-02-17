# 169. Majority Element

**Difficulty:** Easy

## Problem Description
Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Examples

### Example 1
```
Input: nums = [3,2,3]
Output: 3
```

### Example 2
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The majority element always exists in the array.

## Approach
Boyer-Moore Voting Algorithm:
1. Maintain a `result` candidate and a `count`.
2. When `count` hits 0, set the current element as the new candidate.
3. Increment `count` if the current element matches the candidate, otherwise decrement.
4. Early exit: if `count` exceeds `n // 2`, the current candidate is guaranteed to be the majority element.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — single pass through the array.
- **Space Complexity:** `O(1)` — only two variables used.
