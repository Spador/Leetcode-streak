# 152. Maximum Product Subarray

**Difficulty:** Medium

## Problem Description
Given an integer array `nums`, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

## Examples

### Example 1
```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

### Example 2
```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is guaranteed to fit in a 32-bit integer

## Approach
1. Use dynamic programming to track both the current minimum and maximum product at each position.
2. The key insight is that a negative number can flip a minimum product into a maximum product.
3. For each number, we need to consider three possibilities:
   - The number itself
   - The number multiplied by the previous maximum product
   - The number multiplied by the previous minimum product (important for negative numbers)
4. Handle zeros by resetting the current min and max to 1 when encountering a zero (since multiplying by 0 would break the chain).
5. Keep track of the overall maximum product seen so far.

## Algorithm
- Initialize `result = max(nums)` to handle edge cases, `currMin = 1`, and `currMax = 1`.
- For each number `n` in `nums`:
  - If `n == 0`, reset `currMax = 1` and `currMin = 1` (break the product chain).
  - Otherwise:
    - Store `temp = n * currMax` before updating.
    - Update `currMax = max(n * currMax, n * currMin, n)`.
    - Update `currMin = min(temp, n * currMin, n)`.
  - Update `result = max(result, currMax)`.
- Return `result`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` - single pass through the array.
- **Space Complexity:** `O(1)` - only using a few variables regardless of input size.
