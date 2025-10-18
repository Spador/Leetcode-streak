# 131. Palindrome Partitioning

**Difficulty:** Medium

## Problem Description

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

## Examples

### Example 1:
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

### Example 2:
```
Input: s = "a"
Output: [["a"]]
```

## Constraints

- 1 <= s.length <= 16
- s contains only lowercase English letters.

## Approach

This problem can be solved using backtracking:

1. **Backtracking Strategy**: We try to partition the string at every possible position and check if the substring is a palindrome.
2. **Base Case**: When we've processed the entire string, we add the current partition to the result.
3. **Recursive Case**: For each position, we try all possible substrings starting from that position and check if they are palindromes.
4. **Palindrome Check**: We use a helper function to check if a substring is a palindrome.

## Algorithm

1. Start with an empty partition and index 0
2. For each possible ending position from current index to end of string:
   - Check if the substring from current index to ending position is a palindrome
   - If yes, add it to current partition and recursively process the remaining string
   - Backtrack by removing the last added substring
3. When we reach the end of the string, add the current partition to results

## Time Complexity

- **Time**: O(2^n * n) where n is the length of the string
  - In the worst case, we have 2^n possible partitions
  - Each palindrome check takes O(n) time
- **Space**: O(n) for the recursion stack and current partition

## Solution

The solution uses backtracking to generate all possible palindrome partitions by:
- Trying all possible substrings starting from each position
- Checking if each substring is a palindrome
- Recursively processing the remaining string
- Backtracking when a path doesn't lead to a valid solution
