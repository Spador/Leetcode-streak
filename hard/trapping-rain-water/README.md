# 42. Trapping Rain Water

## Problem Description

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

## Examples

### Example 1:
```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

### Example 2:
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Constraints

- `n == height.length`
- `1 <= n <= 2 * 10^4`
- `0 <= height[i] <= 10^5`

## Approach

The solution uses the **two-pointer technique**:

1. Initialize two pointers (`l` and `r`) at the start and end of the array
2. Keep track of the maximum height seen so far from both sides (`lMax` and `rMax`)
3. Move the pointer with the smaller maximum height inward
4. For each position, the trapped water is the difference between the maximum height and current height
5. Continue until the pointers meet

**Key Insight**: Water trapped at any position depends on the minimum of the maximum heights to its left and right. By using two pointers, we can efficiently calculate this without extra space.

## Time Complexity

O(n) - Single pass through the array with two pointers.

## Space Complexity

O(1) - Only using a constant amount of extra space.
