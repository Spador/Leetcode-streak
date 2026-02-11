# 408. Valid Word Abbreviation

**Difficulty:** Easy

## Problem Description
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as `"substitution"` could be abbreviated as (but not limited to):

- `"s10n"` (`"s ubstitutio n"`)
- `"sub4u4"` (`"sub stit u tion"`)
- `"12"` (`"substitution"`)
- `"su3i1u2on"` (`"su bst i t u ti on"`)
- `"substitution"` (no substrings replaced)

The following are **not** valid abbreviations:

- `"s55n"` (the replaced substrings are adjacent)
- `"s010n"` (has leading zeros)
- `"s0ubstitution"` (replaces an empty substring)

Given a string `word` and an abbreviation `abbr`, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

## Examples

### Example 1
```
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
```

### Example 2
```
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
```

## Constraints
- `1 <= word.length <= 20`
- `word` consists of only lowercase English letters.
- `1 <= abbr.length <= 10`
- `abbr` consists of lowercase English letters and digits.

## Approach
Use two pointers, one on `word` and one on `abbr`:

1. If `abbr[a]` is a letter and matches `word[w]`, advance both pointers.
2. If `abbr[a]` is a letter that does **not** match `word[w]`, return `false`.
3. If `abbr[a]` is `'0'`, return `false` (no leading zeros allowed in numbers).
4. Otherwise, parse a positive integer from `abbr` starting at `a` (while the characters are digits), accumulate it in `num`, then advance `w` by `num` (skipping that many characters in `word`).
5. At the end, the abbreviation is valid only if both pointers are exactly at the ends of their strings.

## Time & Space Complexity
- **Time Complexity:** O(n), where n is `len(abbr)` or `len(word)` (single pass).
- **Space Complexity:** O(1) auxiliary.
