# 3315. Construct the Minimum Bitwise Array II

**Difficulty:** Medium

## Problem Description
You are given an array `nums` consisting of `n` prime integers.

You need to construct an array `ans` of length `n`, such that, for each index `i`, the bitwise OR of `ans[i]` and `ans[i] + 1` is equal to `nums[i]`, i.e.

`ans[i] | (ans[i] + 1) == nums[i]`

Additionally, you must minimize each value of `ans[i]` in the resulting array.

If it is not possible to find such a value for `ans[i]` that satisfies the condition, then set `ans[i] = -1`.

## Examples

### Example 1
```
Input: nums = [2,3,5,7]
Output: [-1,1,4,3]
Explanation:
For i = 0, as there is no value for ans[0] that satisfies ans[0] OR (ans[0] + 1) = 2, so ans[0] = -1.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 3 is 1, because 1 OR (1 + 1) = 3.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 5 is 4, because 4 OR (4 + 1) = 5.
For i = 3, the smallest ans[3] that satisfies ans[3] OR (ans[3] + 1) = 7 is 3, because 3 OR (3 + 1) = 7.
```

### Example 2
```
Input: nums = [11,13,31]
Output: [9,12,15]
Explanation:
For i = 0, the smallest ans[0] that satisfies ans[0] OR (ans[0] + 1) = 11 is 9, because 9 OR (9 + 1) = 11.
For i = 1, the smallest ans[1] that satisfies ans[1] OR (ans[1] + 1) = 13 is 12, because 12 OR (12 + 1) = 13.
For i = 2, the smallest ans[2] that satisfies ans[2] OR (ans[2] + 1) = 31 is 15, because 15 OR (15 + 1) = 31.
```

## Constraints
- `1 <= nums.length <= 100`
- `2 <= nums[i] <= 10^9`
- `nums[i]` is a prime number.

## Approach
We need `ans | (ans + 1) == n` for a given prime `n`, and we want the **minimum** such `ans` (or `-1` if impossible).

Key bitwise idea:
- For two consecutive integers `x` and `x + 1`:
  - `x` has some suffix of `1` bits (possibly empty) and then a `0` bit.
  - `x + 1` flips that trailing `1`-suffix to `0`s and sets that `0` bit to `1`.
  - Therefore, `x | (x + 1)` is formed by:
    - all the higher bits of `x` unchanged,
    - the bit where the carry happens becomes `1`,
    - and all lower bits become `1`.

For the minimal `ans` that satisfies `ans | (ans + 1) == n`, we can derive:
- Let `n` be given.
- The lowest set bit of `n + 1` (i.e. `(n + 1) & (-(n + 1))`) tells us how many lower bits need to be `1` in the OR result.
- The formula for minimal `ans` that works is:
  - `ans = n - ((n + 1) & (-(n + 1))) // 2`
- For `n = 2`, this construction is impossible (there is no `ans` such that `ans | (ans + 1) == 2`), so we return `-1`.

Thus for each `n`:
- If `n == 2`, set `ans[i] = -1`.
- Otherwise compute `ans[i] = n - ((n + 1) & (-(n + 1))) // 2`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n = len(nums)`, since we perform `O(1)` work per element.
- **Space Complexity:** `O(1)` extra space beyond the output array.

