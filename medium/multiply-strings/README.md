# 43. Multiply Strings

**Difficulty:** Medium

## Problem Description
Given two non-negative integers `num1` and `num2` as strings, return their product as a string without using built-in big integer libraries or direct integer conversion.

## Examples

### Example 1
```
Input: num1 = "2", num2 = "3"
Output: "6"
```

### Example 2
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints
- `1 <= num1.length, num2.length <= 200`
- Both consist of digits only, no leading zeros except `"0"`.

## Approach
Grade-school multiplication on reversed strings:
1. Reverse both strings so index `i` maps to the ones place.
2. For each pair `(i, j)`, multiply digits and add to `result[i+j]`, carrying overflow to `result[i+j+1]`.
3. Reverse `result`, strip leading zeros, and join as a string.

## Time & Space Complexity
- **Time Complexity:** `O(m * n)`
- **Space Complexity:** `O(m + n)`
