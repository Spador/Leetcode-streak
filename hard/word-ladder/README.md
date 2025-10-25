# 127. Word Ladder

**Difficulty:** Hard

## Problem Description

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or 0 if no such sequence exists.

## Examples

### Example 1:
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
```

### Example 2:
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
```

## Constraints

- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters.
- beginWord != endWord
- All the words in wordList are unique.

## Approach

This problem can be solved using Breadth-First Search (BFS) to find the shortest path:

1. **Pattern Matching**: Create a graph where words are connected if they differ by one character
2. **BFS Traversal**: Use BFS to find the shortest path from beginWord to endWord
3. **Level Processing**: Process each level to count the number of transformations
4. **Early Termination**: Return immediately when endWord is found

## Algorithm

1. Check if endWord exists in wordList (return 0 if not)
2. Build adjacency list using pattern matching:
   - For each word, create patterns by replacing each character with '*'
   - Words sharing the same pattern are connected
3. Use BFS to find shortest path:
   - Start from beginWord
   - Process each level (transformation step)
   - Add unvisited connected words to queue
   - Increment transformation count for each level
4. Return transformation count when endWord is reached

## Implementation Details

- **Pattern Generation**: Create patterns by replacing each character with '*'
- **Graph Construction**: Build connections using pattern matching
- **BFS with Levels**: Process each transformation level separately
- **Visited Tracking**: Avoid revisiting words to prevent cycles
- **Early Check**: Verify endWord exists before processing

## Key Optimizations

- **Pattern Matching**: Efficiently find connected words using wildcard patterns
- **Level-by-level BFS**: Process transformations in batches
- **Visited Set**: Prevent redundant processing of same words
- **Early Termination**: Stop as soon as endWord is found

## Time Complexity

- **Time**: O(M² × N) where M is word length and N is wordList size
  - Pattern generation: O(M × N)
  - BFS traversal: O(M² × N) in worst case
- **Space**: O(M × N) for the adjacency list and BFS queue

## Solution

The solution uses BFS with pattern matching:
- Builds graph using wildcard patterns
- Finds shortest path using level-by-level BFS
- Returns transformation count or 0 if no path exists
