# 139. Word Break

**Difficulty:** Medium

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Examples

### Example 1
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

### Example 2
```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

### Example 3
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Constraints
- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters
- All the strings of `wordDict` are unique

## Approach
1. Use dynamic programming with a bottom-up iterative approach.
2. Create a DP array where `dp[i]` represents whether the substring from index `i` to the end can be segmented into words from the dictionary.
3. Start from the end of the string and work backwards.
4. For each position `i`, check if any word from the dictionary matches the substring starting at `i`.
5. If a word matches and the remaining substring (from `i + word.length`) can be segmented (i.e., `dp[i + word.length]` is true), then `dp[i]` is true.
6. The base case is `dp[len(s)] = True` (empty string can always be segmented).

## Algorithm
- Initialize `dp` array of size `len(s) + 1` with all `False` values.
- Set `dp[len(s)] = True` as base case (empty string is valid).
- Iterate backwards from `len(s) - 1` to `0`:
  - For each word in `wordDict`:
    - Check if the word matches the substring starting at position `i`.
    - If it matches and `dp[i + len(word)]` is `True`, set `dp[i] = True` and break (early exit optimization).
- Return `dp[0]` (whether the entire string can be segmented).

## Time & Space Complexity
- **Time Complexity:** `O(n * m * n)` where `n` is the length of string and `m` is the number of words in dictionary. For each position (n), we check each word (m), and string comparison takes O(n).
- **Space Complexity:** `O(n)` for the DP array.
