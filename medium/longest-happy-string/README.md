# 1405. Longest Happy String

**Difficulty:** Medium

## Problem Description

A string `s` is called happy if it satisfies the following conditions:

- `s` only contains the letters 'a', 'b', and 'c'.
- `s` does not contain any of "aaa", "bbb", or "ccc" as a substring.
- `s` contains at most `a` occurrences of the letter 'a'.
- `s` contains at most `b` occurrences of the letter 'b'.
- `s` contains at most `c` occurrences of the letter 'c'.

Given three integers `a`, `b`, and `c`, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

## Examples

### Example 1:
```
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
```

### Example 2:
```
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
```

## Constraints

- 0 <= a, b, c <= 100
- a + b + c > 0

## Approach

This problem can be solved using a greedy approach with a max heap:

1. **Max Heap**: Use a max heap (min heap with negative values) to always select the character with the most remaining count
2. **Greedy Selection**: Always try to use the character with the highest count
3. **Consecutive Check**: If the last two characters are the same, use the second most frequent character instead
4. **Termination**: Stop when no more characters can be added

## Algorithm

1. Build a max heap with character counts (using negative values for min heap)
2. While heap is not empty:
   - Pop the character with highest count
   - If last two characters are the same as current:
     - If heap is empty, break (can't add more)
     - Pop second character and use it instead
   - Add character to result and decrement count
   - Push character back to heap if count > 0
3. Return the result string

## Implementation Details

- **Max Heap Simulation**: Use min heap with negative counts
- **Consecutive Detection**: Check if last two characters match
- **Greedy Strategy**: Always prefer character with highest count
- **Fallback Mechanism**: Use second character when consecutive limit reached

## Key Optimizations

- **Heap-based Selection**: O(log n) insertion and extraction
- **Greedy Approach**: Maximizes string length by using most frequent characters
- **Early Termination**: Stops when no valid characters can be added

## Time Complexity

- **Time**: O(n log 3) = O(n) where n is total number of characters
  - Each character is processed once
  - Heap operations are O(log 3) = O(1) since only 3 characters
- **Space**: O(1) for the heap (at most 3 elements)

## Solution

The solution uses a greedy approach with max heap:
- Maintains character counts in a max heap
- Greedily selects characters with highest counts
- Avoids three consecutive same characters
- Returns the longest possible happy string
