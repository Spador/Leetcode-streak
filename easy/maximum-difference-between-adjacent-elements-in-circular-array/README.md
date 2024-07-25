# 3423. Maximum Difference Between Adjacent Elements in a Circular Array

## Problem Description

Given a circular array `nums`, find the maximum absolute difference between adjacent elements.

**Note**: In a circular array, the first and last elements are adjacent.

## Examples

### Example 1:
```
Input: nums = [1,2,4]
Output: 3
Explanation:
Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.
```

### Example 2:
```
Input: nums = [-5,-10,-5]
Output: 5
Explanation:
The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.
```

## Constraints

- `2 <= nums.length <= 100`
- `-100 <= nums[i] <= 100`

## Approach

The solution uses a **simple iteration approach**:

1. **Initialize**: Start with the absolute difference between the last and first elements (circular adjacency)
2. **Iterate**: Go through all adjacent pairs in the array
3. **Update Maximum**: Keep track of the maximum absolute difference found
4. **Return Result**: Return the maximum difference

**Key Insight**: Since it's a circular array, we need to check the difference between the last and first elements in addition to all other adjacent pairs.

## Time Complexity

O(n) - Single pass through the array to check all adjacent pairs.

## Space Complexity

O(1) - Only using a constant amount of extra space for tracking the maximum difference.
