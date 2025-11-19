# 269. Alien Dictionary

**Difficulty:** Hard

## Problem Description
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary. Now it is claimed that the strings in `words` are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in `words` cannot correspond to any order of letters, return `""`.

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

## Examples

### Example 1
```
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

### Example 2
```
Input: words = ["z","x"]
Output: "zx"
```

### Example 3
```
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

## Constraints
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 100`
- `words[i]` consists of only lowercase English letters

## Approach
1. Build a directed graph representing the ordering constraints between characters based on adjacent word comparisons.
2. For each pair of adjacent words, find the first differing character and add an edge from the first word's character to the second word's character.
3. Check for invalid cases: if a longer word is a prefix of a shorter word that comes after it, the ordering is invalid.
4. Use topological sorting with DFS to detect cycles (invalid ordering) and produce the lexicographical order.
5. If a cycle is detected, return an empty string; otherwise, return the topologically sorted characters.

## Algorithm
- Initialize an adjacency list for all characters present in the words.
- Compare adjacent words to build ordering constraints:
  - Find the first position where characters differ.
  - Add an edge from the character in the first word to the character in the second word.
  - Handle the invalid case where a longer word is a prefix of a shorter subsequent word.
- Perform DFS-based topological sorting:
  - Use a visit state map: `True` for currently in path (cycle detection), `False` for completed.
  - If a cycle is detected during DFS, return empty string.
  - Collect characters in reverse topological order and reverse the result.

## Time & Space Complexity
- **Time Complexity:** `O(C)` where C is the total number of characters across all words, for building the graph and performing topological sort.
- **Space Complexity:** `O(1)` for the adjacency list and visit tracking (at most 26 characters), plus `O(C)` for the result.
