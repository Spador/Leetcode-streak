# 190. Reverse Bits

**Difficulty:** Easy

## Problem Description
Reverse the bits of a given 32-bit unsigned integer.

## Examples

### Example 1
```
Input:  n = 43261596   (00000010100101000001111010011100)
Output: 964176192      (00111001011110000010100101000000)
```

### Example 2
```
Input:  n = 2147483644  (01111111111111111111111111111100)
Output: 1073741822      (00111111111111111111111111111110)
```

## Constraints
- `0 <= n <= 2^31 - 2`
- `n` is even.

## Approach
Bit-by-bit reversal:
1. Iterate over all 32 bit positions.
2. Extract bit `i` from `n` using `(n >> i) & 1`.
3. Place it at position `31 - i` in `result` using `bit << (31 - i)`.
4. OR it into `result` to accumulate the reversed bits.

## Time & Space Complexity
- **Time Complexity:** `O(1)` — always exactly 32 iterations.
- **Space Complexity:** `O(1)` — only a result integer used.
