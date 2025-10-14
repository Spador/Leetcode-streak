# 78. Subsets

**Difficulty:** Medium

## Problem Description

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Examples

**Example 1:**
```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2:**
```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are unique.

## Approach

Use backtracking to explore inclusion/exclusion for each element:
- Maintain a current `subset` list.
- At each index, choose to include `nums[index]` or skip it, and recurse to the next index.
- When reaching the end, add a copy of `subset` to the results.

This generates all `2^n` subsets without duplicates since input elements are unique.

### Complexity
- Time: O(n * 2^n), as each subset copy costs up to O(n) and there are 2^n subsets.
- Space: O(n) recursion depth (excluding output).
