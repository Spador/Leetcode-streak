# 678. Valid Parenthesis String

**Difficulty:** Medium

## Problem Description
Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` if `s` is valid.

The following rules define a valid string:

1. Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
2. Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
3. Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
4. `'*'` could be treated as:
   - a single right parenthesis `')'`, or
   - a single left parenthesis `'('`, or
   - an empty string `""`.

## Examples

### Example 1
```
Input: s = "()"
Output: true
```

### Example 2
```
Input: s = "(*)"
Output: true
```

### Example 3
```
Input: s = "(*))"
Output: true
```

## Constraints
- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'` or `'*'`.

## Approach
We can solve this using a greedy range-tracking technique instead of backtracking over all interpretations of `'*'`.

Maintain two values:
- `minOpen`: the **minimum** possible number of unmatched `'('` at this point (assuming `'*'` becomes `')'` or empty as much as possible).
- `maxOpen`: the **maximum** possible number of unmatched `'('` at this point (assuming `'*'` becomes `'('` as much as possible).

Scan `s` from left to right:
- If `c == '('`:
  - `minOpen += 1`, `maxOpen += 1`
- If `c == ')'`:
  - `minOpen -= 1`, `maxOpen -= 1`
- If `c == '*'`:
  - `minOpen -= 1` (treating it as `')'` or empty in the best case)
  - `maxOpen += 1` (treating it as `'('` in the worst case)

Additional rules:
- If `maxOpen < 0` at any point, we have more `')'` than possible `'('`, so return `False`.
- If `minOpen < 0`, clamp it to `0` (we can't have fewer than 0 unmatched `'('`).

At the end:
- If `minOpen == 0`, it means there exists some interpretation of `'*'` that makes the string fully balanced, so return `True`.
- Otherwise, return `False`.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(s)`, since we scan the string once.
- **Space Complexity:** `O(1)`, using only a couple of counters.

