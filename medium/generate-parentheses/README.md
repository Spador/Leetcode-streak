# 22. Generate Parentheses

**Difficulty:** Medium

## Problem Description
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

### Example 1
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2
```
Input: n = 1
Output: ["()"]
```

## Constraints
- `1 <= n <= 8`

## Approach
We use **backtracking** to build all valid strings of length `2 * n`.

Rules:
- We can add an `'('` as long as the number of open parentheses used so far is less than `n`.
- We can add a `')'` as long as the number of closing parentheses is less than the number of open ones (to keep the string valid at every prefix).
- A string is complete and valid when we have used exactly `n` open and `n` close parentheses.

Algorithm:
1. Maintain:
   - a `stack` (list of characters) representing the current string being built,
   - a `result` list to collect all valid strings.
2. Define a recursive function `backtrack(openP, closeP)` where:
   - `openP` is the number of `'('` used so far,
   - `closeP` is the number of `')'` used so far.
3. Base case:
   - If `openP == closeP == n`, append `"".join(stack)` to `result` and return.
4. Recursive steps:
   - If `openP < n`:
     - Append `'('` to `stack`, call `backtrack(openP + 1, closeP)`, then pop from `stack`.
   - If `closeP < openP`:
     - Append `')'` to `stack`, call `backtrack(openP, closeP + 1)`, then pop from `stack`.
5. Start with `backtrack(0, 0)` and return `result`.

## Time & Space Complexity
- **Time Complexity:** `O(C_n)` where `C_n` is the `n`th Catalan number, since that's the number of valid parentheses combinations.
- **Space Complexity:** `O(n)` for the recursion stack and current `stack` content (excluding the space for the `result` list).

