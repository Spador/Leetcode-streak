# 1545. Find Kth Bit in Nth Binary String

**Difficulty:** Medium

## Problem Description
The binary string `Sn` is built recursively: `S1 = "0"`, `Si = S(i-1) + "1" + reverse(invert(S(i-1)))`. Return the `k`th bit in `Sn`.

## Examples

### Example 1
```
Input: n = 3, k = 1
Output: "0"
```

### Example 2
```
Input: n = 4, k = 11
Output: "1"
```

## Constraints
- `1 <= n <= 20`
- `1 <= k <= 2^n - 1`

## Approach

### Brute Force
Build up each string iteratively from S1 to Sn and index directly. Only feasible for small `n`.
- **Time:** `O(2^n)` | **Space:** `O(2^n)`

### Optimised (Iterative + Recursive)
Exploit the structure of `Sn`: length is `2^n - 1`, the middle bit is always `1`, the left half is `S(n-1)`, and the right half is the inverted-reverse of `S(n-1)`.
1. If `k` is in the left half, recurse/iterate with same parity.
2. If `k` is the middle bit, return `1` (flipped if inverted).
3. If `k` is in the right half, mirror it to the left half and flip the invert flag.
- **Time:** `O(n)` | **Space:** `O(1)` iterative / `O(n)` recursive
