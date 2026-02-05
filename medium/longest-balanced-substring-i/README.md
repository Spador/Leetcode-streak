# 3713. Longest Balanced Substring I

**Difficulty:** Medium

## Problem Description
You are given a string `s` consisting of lowercase English letters.

A substring of `s` is called **balanced** if all distinct characters in the substring appear the **same number of times**.

Return the length of the **longest balanced substring** of `s`.

## Examples

### Example 1
```
Input: s = "abbac"
Output: 4
Explanation:
The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.
```

### Example 2
```
Input: s = "zzabccy"
Output: 4
Explanation:
The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.
```

### Example 3
```
Input: s = "aba"
Output: 2
Explanation:
One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".
```

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Approach
We can brute-force over all substrings and check if they are balanced using a frequency counter:

1. Initialize `result = 0`.
2. For each starting index `i` from `0` to `len(s) - 1`:
   - Initialize a frequency dictionary `count` (e.g. `defaultdict(int)`).
   - For each ending index `j` from `i` to `len(s) - 1`:
     - Increment `count[s[j]]`.
     - If all values in `count` are equal (i.e., `len(set(count.values())) == 1`), then the substring `s[i:j+1]` is balanced:
       - Update `result = max(result, j - i + 1)`.
3. Return `result`.

This directly follows the definition: within each substring, all distinct characters must have the same frequency.

## Time & Space Complexity
- **Time Complexity:** `O(n^2 * k)` in the naive implementation, where `n = len(s)` and `k` is the number of distinct characters in the substring (at most 26). With `len(set(count.values()))` each step, the inner check is `O(k)`, and we have `O(n^2)` substrings.
- **Space Complexity:** `O(k)` for the frequency dictionary per starting index.
