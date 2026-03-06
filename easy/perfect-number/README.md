# 507. Perfect Number

**Difficulty:** Easy

## Problem Description
Return `true` if `num` equals the sum of its positive divisors excluding itself.

## Examples

### Example 1
```
Input: num = 28
Output: true  (1 + 2 + 4 + 7 + 14 = 28)
```

### Example 2
```
Input: num = 7
Output: false
```

## Constraints
- `1 <= num <= 10^8`

## Approach
Iterate up to `sqrt(num)`. For each divisor `i`, add both `i` and `num // i` (unless they're equal). Sum starts at 1 (always a divisor).

## Time & Space Complexity
- **Time Complexity:** `O(sqrt(n))`
- **Space Complexity:** `O(1)`
