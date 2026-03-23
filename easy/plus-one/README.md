# 66. Plus One

**Difficulty:** Easy

## Problem Description
Given a large integer represented as an array of digits (most to least significant), increment it by one and return the resulting array.

## Examples

### Example 1
```
Input: digits = [1,2,3]
Output: [1,2,4]
```

### Example 2
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
```

### Example 3
```
Input: digits = [9]
Output: [1,0]
```

## Constraints
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- No leading zeros.

## Approach
1. Traverse from the last digit to the first.
2. If adding 1 doesn't cause a carry, increment and return.
3. If it does (digit is 9), set it to 0 and continue.
4. If all digits were 9, prepend 1 to the zeroed array.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` extra (result reuses input array)
