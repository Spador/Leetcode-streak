# 3507. Minimum Pair Removal to Sort Array I

**Difficulty:** Easy

## Problem Description
Given an array `nums`, you can perform the following operation any number of times:

1. Select the adjacent pair with the minimum sum in `nums`. If multiple such pairs exist, choose the leftmost one.
2. Replace the pair with their sum.

Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

## Examples

### Example 1
```
Input: nums = [5,2,3,1]
Output: 2
Explanation:
The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
The array nums became non-decreasing in two operations.
```

### Example 2
```
Input: nums = [1,2,2]
Output: 0
Explanation:
The array nums is already sorted.
```

## Constraints
- `1 <= nums.length <= 50`
- `-1000 <= nums[i] <= 1000`

## Approach
We repeatedly apply the described operation until the array becomes non-decreasing:

1. Define a helper function `isSorted(nums)` that checks if the array is non-decreasing.
2. While `nums` is not sorted:
   - Find the adjacent pair with the **minimum sum**, breaking ties by taking the leftmost such pair.
   - Replace the left element of that pair with the sum and remove the right element.
   - Increment an operation counter `ops`.
3. Once `nums` is non-decreasing, return `ops`.

This simulates exactly the process described in the problem statement.

## Time & Space Complexity
Let `n = len(nums)`.
- Each `isSorted` check is `O(n)`.
- Finding the minimum-sum adjacent pair is `O(n)`.
- We perform at most `n - 1` operations (each reduces the array length by 1).

Thus:
- **Time Complexity:** `O(n^2)` in the worst case.
- **Space Complexity:** `O(1)` extra space (modifying `nums` in-place aside from the recursion stack, which we don't use here).
