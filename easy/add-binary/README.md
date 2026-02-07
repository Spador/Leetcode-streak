# 67. Add Binary

**Difficulty:** Easy

## Problem Description
Given two binary strings `a` and `b`, return their sum as a binary string.

## Examples

### Example 1
```
Input: a = "11", b = "1"
Output: "100"
```

### Example 2
```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Constraints
- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## Approach
We simulate binary addition from right to left using a carry, similar to how we add numbers by hand:

1. Reverse both strings `a` and `b` so we can iterate from least significant bit to most significant bit using simple indices.
2. Initialize `carry = 0` and an empty `result` string.
3. For each index `i` from `0` to `max(len(a), len(b)) - 1`:
   - Let `adigit` be the bit from `a` at position `i` (or `0` if `i` is out of range).
   - Let `bdigit` be the bit from `b` at position `i` (or `0` if `i` is out of range).
   - Compute `total = adigit + bdigit + carry`.
   - The current result bit is `total % 2`.
   - The new `carry` is `total // 2`.
   - Prepend the current result bit to the `result` string.
4. After the loop, if `carry` is `1`, prepend `'1'` to the result.
5. Return the final `result` string.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n = max(len(a), len(b))`.
- **Space Complexity:** `O(n)` for the result string.
