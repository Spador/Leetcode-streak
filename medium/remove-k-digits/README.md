# 402. Remove K Digits

**Difficulty:** Medium

## Problem Description
Given string `num` representing a non-negative integer and an integer `k`, return the smallest possible integer after removing `k` digits from `num`.

## Examples

### Example 1
```
Input: num = "1432219", k = 3
Output: "1219"
```

### Example 2
```
Input: num = "10200", k = 1
Output: "200"
```

### Example 3
```
Input: num = "10", k = 2
Output: "0"
```

## Constraints
- `1 <= k <= num.length <= 10^5`
- `num` consists of only digits.
- `num` does not have any leading zeros except for the zero itself.

## Approach
Use a monotonic stack (ascending order). For each digit, pop the stack while the top is greater than the current digit and `k > 0`. Trim remaining `k` digits from the end, strip leading zeros, return "0" if empty.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`
