# 387. First Unique Character in a String

**Difficulty:** Easy

## Problem Description
Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.

## Examples

### Example 1
```
Input: s = "leetcode"
Output: 0
```

### Example 2
```
Input: s = "loveleetcode"
Output: 2
```

### Example 3
```
Input: s = "aabb"
Output: -1
```

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Approach
Count character frequencies with a hashmap. Then iterate the string again and return the index of the first character with count 1.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` (at most 26 keys)
