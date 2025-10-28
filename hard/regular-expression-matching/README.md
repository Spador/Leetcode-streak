# 10. Regular Expression Matching

**Difficulty:** Hard

## Problem Description

Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` and `'*'` where:

- `'.'` Matches any single character.
- `'*'` Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

## Examples

### Example 1:
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2:
```
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
```

### Example 3:
```
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
```

## Constraints

- 1 <= s.length <= 20
- 1 <= p.length <= 20
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

## Approach

This problem can be solved using Dynamic Programming with memoization (top-down approach):

1. **State Definition**: Use (i, j) to represent matching s[i:] with p[j:]
2. **Base Cases**: 
   - If both strings are exhausted, return true
   - If pattern is exhausted but string isn't, return false
3. **Character Matching**: Check if current characters match (exact match or '.')
4. **Star Handling**: When encountering '*', consider two cases:
   - Don't use '*' (skip the pattern)
   - Use '*' (match one or more characters)
5. **Memoization**: Cache results to avoid redundant computations

## Algorithm

1. Initialize memoization cache
2. Define recursive function dfs(i, j):
   - If (i, j) in cache, return cached result
   - If both indices exhausted, return true
   - If pattern exhausted but string isn't, return false
   - Check if current characters match
   - If next character is '*':
     - Try skipping '*' (don't use it)
     - Try using '*' (match one or more)
   - If characters match, advance both indices
   - Otherwise, return false
3. Return result of dfs(0, 0)

## Implementation Details

- **Top-Down DP**: Recursive approach with memoization
- **Two-pointer Technique**: Track positions in both string and pattern
- **Star Handling**: Consider both using and not using the star
- **Memoization**: Cache subproblem results for efficiency

## Key Optimizations

- **Memoization**: Avoid recomputing same subproblems
- **Early Termination**: Return immediately when base cases are met
- **Efficient State Representation**: Use tuple (i, j) as cache key

## Time Complexity

- **Time**: O(m × n) where m is length of s and n is length of p
  - Each state (i, j) is computed at most once
- **Space**: O(m × n) for the memoization cache

## Solution

The solution uses top-down dynamic programming with memoization:
- Recursively matches string and pattern with caching
- Handles '.' and '*' special characters correctly
- Returns true if entire string matches the pattern
