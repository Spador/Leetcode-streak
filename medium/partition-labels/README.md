# 763. Partition Labels

**Difficulty:** Medium

## Problem Description
You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in **at most one part**.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be `s`.

Return a list of integers representing the size of these parts.

## Examples

### Example 1
```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into fewer parts.
```

### Example 2
```
Input: s = "eccbbbbdec"
Output: [10]
```

## Constraints
- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Approach
We want to cut `s` into segments such that no character spans across segments. A greedy strategy works:

1. First, record the **last occurrence** index of each character in `s` in a dictionary `last`.
2. Scan the string from left to right, maintaining:
   - `currEnd`: the farthest last occurrence of any character seen in the current segment.
   - `size`: the current segment length.
3. For each index `i`:
   - Increment `size` by 1.
   - Update `currEnd = max(currEnd, last[s[i]])`.
   - If `i == currEnd`, it means all characters seen so far end within this range, so we can close a partition:
     - Append `size` to the result list.
     - Reset `size` to 0 for the next partition.
4. Optionally, if we already know `currEnd` is the last index of the string, we can early-return the result with the remaining size (as in the optimization in your solution).

## Algorithm
- Build a dictionary `last` mapping each character to its last index in `s`.
- Initialize `size = 0`, `currEnd = 0`, `result = []`.
- Loop `i` from `0` to `len(s) - 1`:
  - `size += 1`
  - `currEnd = max(currEnd, last[s[i]])`
  - If `i == currEnd`:
    - Append `size` to `result`
    - Reset `size = 0`
  - (Optional optimization) If `i != len(s) - 1` and `currEnd == len(s) - 1`, append the remaining size and return.
- Return `result`.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(s)`, since we scan the string a constant number of times.
- **Space Complexity:** `O(1)` extra space (at most 26 entries in `last` for lowercase letters), plus the output list.

