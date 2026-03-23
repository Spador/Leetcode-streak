# 383. Ransom Note

**Difficulty:** Easy

## Problem Description
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed using letters from `magazine` (each letter used at most once).

## Examples

### Example 1
```
Input: ransomNote = "a", magazine = "b"
Output: false
```

### Example 2
```
Input: ransomNote = "aa", magazine = "ab"
Output: false
```

### Example 3
```
Input: ransomNote = "aa", magazine = "aab"
Output: true
```

## Constraints
- `1 <= ransomNote.length, magazine.length <= 10^5`
- Both strings consist of lowercase English letters.

## Approach
1. Count character frequencies in `magazine` using a hashmap.
2. For each letter in `ransomNote`, check it exists with count > 0, then decrement.
3. Return `false` if any letter is unavailable.

## Time & Space Complexity
- **Time Complexity:** `O(n + m)`
- **Space Complexity:** `O(1)` — at most 26 keys in the map
