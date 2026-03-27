# 977. Squares of a Sorted Array

**Difficulty:** Easy

## Problem Description
Given a sorted integer array, return a new array of the squares of each number, also sorted in non-decreasing order.

## Examples

### Example 1
```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

### Example 2
```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Approach
Two pointers from both ends, filling result from the back:
1. Compare absolute values at `left` and `right`.
2. Place the larger square at the current tail of `result` and move that pointer inward.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
