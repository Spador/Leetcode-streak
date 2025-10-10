# 211. Design Add and Search Words Data Structure

## Problem Description

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds word to the data structure, it can be matched later.
- `bool search(word)` Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

## Examples

### Example:
```
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## Constraints

- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.

## Approach

This problem can be solved using a **Trie (Prefix Tree)** data structure with modifications to handle wildcard matching:

### Data Structure:
- **TrieNode**: Contains a dictionary of children (character → TrieNode) and a boolean flag `isEnd`
- **WordDictionary**: Contains a root TrieNode

### Operations:

#### AddWord:
1. Start from root
2. For each character in the word, traverse or create the corresponding child node
3. Mark the final node as a complete word (`isEnd = True`)

#### Search:
1. Use recursive DFS with index parameter to handle wildcard matching
2. For each character in the search word starting from index j:
   - If it's a regular character, traverse to the corresponding child node
   - If it's a dot ('.'), recursively search all possible child nodes with next index
3. Return `True` if we reach the end and the final node is marked as a complete word

### Key Insights:
- **Trie Structure**: Each path from root to a node represents a prefix
- **Wildcard Handling**: Use recursive DFS with index parameter to explore all possible paths when encountering dots
- **Word Marking**: Use `isEnd` flag to distinguish between prefixes and complete words
- **Index-based DFS**: The recursive function takes a starting index to efficiently handle wildcard matching

### Time Complexity:
- **AddWord**: O(m) where m is the length of the word
- **Search**: O(n * 26^k) where n is the number of words, k is the number of dots
- In the worst case with many dots, it could be exponential

### Space Complexity: O(ALPHABET_SIZE * N * M)
- Where N is the number of words and M is the average length of words
- Trie storage for all inserted words
