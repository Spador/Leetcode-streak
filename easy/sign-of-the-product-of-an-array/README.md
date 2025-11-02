# 1822. Sign of the Product of an Array

**Difficulty:** Easy

## Problem Description

Implement a function `signFunc(x)` that returns:

- 1 if x is positive.
- -1 if x is negative.
- 0 if x is equal to 0.

You are given an integer array `nums`. Let product be the product of all values in the array `nums`.

Return `signFunc(product)`.

## Examples

### Example 1:
```
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
```

### Example 2:
```
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
```

### Example 3:
```
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
```

## Constraints

- 1 <= nums.length <= 1000
- -100 <= nums[i] <= 100

## Approach

This problem can be solved without actually computing the product:

1. **Zero Check**: If any element is 0, product is 0, return 0
2. **Negative Count**: Count the number of negative numbers
3. **Sign Determination**: If count of negatives is even, product is positive (return 1), otherwise negative (return -1)

## Algorithm

1. Initialize negative count to 0
2. Iterate through array:
   - If element is 0, return 0 immediately
   - If element is negative, increment negative count
3. If negative count is even, return 1, else return -1

## Implementation Details

- **Early Termination**: Return 0 immediately if zero is found
- **Negative Counting**: Track number of negative numbers
- **Parity Check**: Even negatives = positive product, odd negatives = negative product

## Key Optimizations

- **O(n) Time**: Single pass through array
- **O(1) Space**: Only track negative count
- **No Multiplication**: Avoids potential overflow by not computing actual product

## Time Complexity

- **Time**: O(n) where n is the length of the array
  - Single pass through the array
- **Space**: O(1) for the negative count

## Solution

The solution counts negative numbers:
- Returns 0 if any element is 0
- Counts negative numbers
- Returns 1 if even negatives, -1 if odd negatives
