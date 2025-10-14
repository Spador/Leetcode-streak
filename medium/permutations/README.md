# 46. Permutations

**Difficulty:** Medium

## Problem Description

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

## Examples

**Example 1:**
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2:**
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3:**
```
Input: nums = [1]
Output: [[1]]
```

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are unique.

## Approach

Use recursion with element swapping:
- Base case: when array length is 1, return the array wrapped in a list.
- For each position, extract an element, recursively generate permutations of the remaining elements, then append the extracted element to each permutation.
- Restore the element back to the array after processing.

This generates all `n!` permutations by systematically trying each element in each position.

### Complexity
- Time: O(n! * n), where n! is the number of permutations and n is the cost of copying/creating each permutation.
- Space: O(n!) for storing all permutations, plus O(n) recursion depth.
