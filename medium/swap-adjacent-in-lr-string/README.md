# 777. Swap Adjacent in LR String

**Difficulty:** Medium

## Problem Description
In a string of 'L', 'R', 'X' characters, a move is replacing "XL" with "LX" or "RX" with "XR". Given `start` and `result`, return `True` if `start` can be transformed into `result`.

## Examples

### Example 1
```
Input: start = "RXXLRXRXL", result = "XRLXXRRLX"
Output: true
```

### Example 2
```
Input: start = "X", result = "L"
Output: false
```

## Constraints
- `1 <= start.length <= 10^4`
- `start.length == result.length`
- Both strings consist only of 'L', 'R', 'X'.

## Approach
Use two pointers, skipping 'X' in both strings. At each non-X pair: characters must match, 'L' can only move left (i >= j), 'R' can only move right (i <= j).

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`
