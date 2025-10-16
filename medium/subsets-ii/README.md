# 90. Subsets II

**Difficulty:** Medium

## Problem Description

Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

## Examples

### Example 1:
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```

### Example 2:
```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`

## Approach

This problem is similar to the regular Subsets problem, but with the added complexity of handling duplicates. The key insight is to sort the array first and then use backtracking with duplicate skipping.

### Algorithm:
1. **Sort the array** to group duplicates together
2. **Use backtracking** to generate all possible subsets
3. **Skip duplicates** by advancing the index when we encounter the same element multiple times
4. **Two choices at each step:**
   - Include the current element
   - Skip the current element and all its duplicates

### Time Complexity
- **Time:** O(2^n * n) where n is the length of the array
- **Space:** O(2^n * n) for storing all subsets

### Space Complexity
- **Space:** O(n) for the recursion stack

## Solution Strategy

The solution uses a backtracking approach with duplicate handling:

1. Sort the input array to group duplicates
2. For each position, we have two choices:
   - Include the current element
   - Skip the current element and all its duplicates
3. When skipping, we advance the index past all duplicate elements
4. This ensures we don't generate duplicate subsets

This approach efficiently handles the duplicate constraint while maintaining the backtracking structure.
