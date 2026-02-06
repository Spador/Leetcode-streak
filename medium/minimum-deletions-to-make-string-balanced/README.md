# 1653. Minimum Deletions to Make String Balanced

**Difficulty:** Medium

## Problem Description
You are given a string `s` consisting only of characters `'a'` and `'b'`.

You can delete any number of characters in `s` to make `s` balanced.

`s` is balanced if there is no pair of indices `(i, j)` such that `i < j` and `s[i] = 'b'` and `s[j] = 'a'` (i.e., no `'b'` appears before an `'a'`).

Return the minimum number of deletions needed to make `s` balanced.

## Examples

### Example 1
```
Input: s = "aababbab"
Output: 2
Explanation: You can either:
- Delete the characters at positions 2 and 6 ("aababbab" -> "aaabbb"), or
- Delete the characters at positions 3 and 6 ("aababbab" -> "aabbbb").
```

### Example 2
```
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
```

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is `'a'` or `'b'`.

## Approach
We want to minimize deletions so that all `'b'`s come before all `'a'`s.

We can think of choosing a split point in the string where:
- All `'b'`s to the **left** of the split are kept (delete any `'a'`s there).
- All `'a'`s to the **right** of the split are kept (delete any `'b'`s there).

Instead of trying all splits explicitly, we can compute this in one pass using counts:

1. First, count how many `'a'`s are in the whole string — call this `a_count_right`.
2. Initialize `b_count_left = 0` and `result = len(s)`.
3. Iterate through `s` from left to right:
   - For each character `ch` at index `i`:
     - If `ch == 'a'`, one `'a'` moves from the right side to the left side, so decrement `a_count_right` by 1.
     - The number of deletions needed if we split **after** this position is:
       - `b_count_left` (delete all `'b'`s on the left side that appear before some `'a'`), plus
       - `a_count_right` (delete all remaining `'a'`s on the right side if we wanted all `'b'`s first).
     - Update `result = min(result, b_count_left + a_count_right)`.
     - If `ch == 'b'`, increment `b_count_left` by 1.
4. Return `result`.

This effectively tries all split positions in a single pass.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n = len(s)`.
- **Space Complexity:** `O(1)` extra space.
