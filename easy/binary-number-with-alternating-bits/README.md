# 693. Binary Number with Alternating Bits

**Difficulty:** Easy

## Problem Description
Given a positive integer, return `true` if its binary representation has alternating bits (no two adjacent bits are the same).

## Examples

### Example 1
```
Input: n = 5   (101)
Output: true
```

### Example 2
```
Input: n = 7   (111)
Output: false
```

### Example 3
```
Input: n = 11  (1011)
Output: false
```

## Constraints
- `1 <= n <= 2^31 - 1`

## Approach
Extract bits one at a time from LSB. If any adjacent pair XOR to something other than 1, return false.

## Time & Space Complexity
- **Time Complexity:** `O(log n)`
- **Space Complexity:** `O(1)`
