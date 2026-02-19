# 118. Pascal's Triangle

**Difficulty:** Easy

## Problem Description
Given an integer `numRows`, return the first `numRows` of Pascal's triangle, where each number is the sum of the two numbers directly above it.

## Examples

### Example 1
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

### Example 2
```
Input: numRows = 1
Output: [[1]]
```

## Constraints
- `1 <= numRows <= 30`

## Approach
1. Start with `result = [[1]]`.
2. For each new row, pad the previous row with a `0` on both sides.
3. Each element of the new row is the sum of adjacent elements in the padded row.
4. Append the new row to result and repeat.

## Time & Space Complexity
- **Time Complexity:** `O(numRows^2)` — each row has one more element than the last.
- **Space Complexity:** `O(numRows^2)` — storing all rows in the result.
