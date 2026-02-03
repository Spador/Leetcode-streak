# 205. Isomorphic Strings

**Difficulty:** Easy

## Problem Description
Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

## Examples

### Example 1
```
Input: s = "egg", t = "add"
Output: true
```

### Example 2
```
Input: s = "f11", t = "b23"
Output: false
```

### Example 3
```
Input: s = "paper", t = "title"
Output: true
```

## Constraints
- `1 <= s.length <= 5 * 10^4`
- `t.length == s.length`
- `s` and `t` consist of any valid ASCII character.

## Approach
We need to ensure a **one-to-one mapping** between characters of `s` and characters of `t`:

- Each character in `s` must always map to the **same** character in `t`.
- No two different characters in `s` may map to the **same** character in `t`.

Algorithm:
1. Use two dictionaries:
   - `Smap` to map characters from `s` to `t`.
   - `Tmap` to map characters from `t` to `s`.
2. Iterate over the indices of the strings:
   - For each index `i`:
     - If `s[i]` is not in `Smap`, set `Smap[s[i]] = t[i]`. Otherwise, check that `Smap[s[i]] == t[i]`; if not, return `False`.
     - Similarly, if `t[i]` is not in `Tmap`, set `Tmap[t[i]] = s[i]`. Otherwise, check that `Tmap[t[i]] == s[i]`; if not, return `False`.
3. If we finish the loop without conflicts, return `True`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` where `n = len(s)`, since we make a single pass through both strings.
- **Space Complexity:** `O(k)` where `k` is the number of distinct characters seen (bounded by the character set size), for the two dictionaries.
