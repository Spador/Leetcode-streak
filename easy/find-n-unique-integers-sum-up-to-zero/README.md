# 1304. Find N Unique Integers Sum up to Zero

**Difficulty:** Easy

## Problem Description

Given an integer `n`, return any array containing `n` unique integers such that they add up to 0.

## Examples

### Example 1:
```
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
```

### Example 2:
```
Input: n = 3
Output: [-1,0,1]
```

### Example 3:
```
Input: n = 1
Output: [0]
```

## Constraints

- 1 <= n <= 1000

## Approach

This problem can be solved using a simple mathematical approach:

1. **Odd n**: Use symmetric pairs around zero (e.g., [-2, -1, 0, 1, 2])
2. **Even n**: Use consecutive positive integers and their negative sum
3. **Special Case**: When n = 1, return [0]

## Algorithm

1. If n is odd:
   - Generate symmetric integers from -(n//2) to (n//2)
   - This naturally includes 0 and sums to 0
2. If n is even:
   - Generate consecutive positive integers from 1 to n-1
   - Add the negative of their sum as the last element
   - This ensures all integers are unique and sum to 0

## Implementation Details

- **Odd Case**: Use range from -(n//2) to (n//2) inclusive
- **Even Case**: Generate n-1 positive integers, then add negative sum
- **Uniqueness**: All generated integers are guaranteed to be unique

## Key Optimizations

- **O(n) Time**: Single pass to generate the array
- **O(n) Space**: Store n integers in result array
- **Simple Logic**: Straightforward mathematical approach

## Time Complexity

- **Time**: O(n) where n is the input integer
  - Generate n integers in the result array
- **Space**: O(n) for the result array

## Solution

The solution uses a mathematical approach:
- For odd n, generates symmetric integers around zero
- For even n, generates positive integers and adds negative sum
- Returns array of n unique integers that sum to zero
