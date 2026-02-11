# 1249. Minimum Remove to Make Valid Parentheses

**Difficulty:** Medium

## Problem Description
Given a string `s` of `'('`, `')'` and lowercase English characters.

Your task is to **remove the minimum number of parentheses** (`'('` or `')'`, in any positions) so that the resulting parentheses string is **valid** and return **any valid string**.

Formally, a parentheses string is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as **AB** (A concatenated with B), where A and B are valid strings, or
- It can be written as **(A)**, where A is a valid string.

## Examples

### Example 1
```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
```

### Example 2
```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

### Example 3
```
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
```

## Constraints
- `1 <= s.length <= 10^5`
- `s[i]` is either `'('`, `')'`, or lowercase English letter.

## Approach
Use a stack to track indices of `'('`. Build a result array (initially empty strings). For each character: on `'('` push index; on `')'` pop if stack non-empty and mark both positions in result, else skip (invalid `')'`); for letters copy to result. Only indices that got written (matched parens or letters) contribute; join the array. Unmatched `'('` indices stay as `""` and are omitted in the final string.

## Time & Space Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) for result and stack
