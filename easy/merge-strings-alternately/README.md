# 1768. Merge Strings Alternately

**Difficulty:** Easy

## Problem Description
Given two strings `word1` and `word2`, merge them by alternating characters starting with `word1`. Append the remaining characters of the longer string at the end.

## Examples

### Example 1
```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
```

### Example 2
```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
```

### Example 3
```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```

## Constraints
- `1 <= word1.length, word2.length <= 100`
- Both strings consist of lowercase English letters.

## Approach
1. Use two pointers to alternate characters from both strings.
2. Append leftover characters from the longer string at the end.

## Time & Space Complexity
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(n + m)`
