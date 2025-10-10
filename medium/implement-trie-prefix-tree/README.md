# 208. Implement Trie (Prefix Tree)

## Problem Description

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string word into the trie.
- `boolean search(String word)` Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- `boolean startsWith(String prefix)` Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

## Examples

### Example 1:
```
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## Constraints

- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.

## Approach

The solution implements a Trie (Prefix Tree) data structure using a tree of nodes where each node represents a character:

### Data Structure:
- **TrieNode**: Contains a dictionary of children (character → TrieNode) and a boolean flag `isWord`
- **Trie**: Contains a root TrieNode

### Operations:

#### Insert:
1. Start from root
2. For each character in the word, traverse or create the corresponding child node
3. Mark the final node as a complete word (`isWord = True`)

#### Search:
1. Start from root
2. For each character in the word, traverse to the corresponding child node
3. Return `True` if we reach the end and the final node is marked as a complete word

#### StartsWith:
1. Start from root
2. For each character in the prefix, traverse to the corresponding child node
3. Return `True` if we can traverse the entire prefix (regardless of whether it's a complete word)

### Key Insights:
- **Tree Structure**: Each path from root to a node represents a prefix
- **Word Marking**: Use `isWord` flag to distinguish between prefixes and complete words
- **Efficient Lookup**: O(m) time complexity where m is the length of the word/prefix

### Time Complexity:
- **Insert**: O(m) where m is the length of the word
- **Search**: O(m) where m is the length of the word
- **StartsWith**: O(m) where m is the length of the prefix

### Space Complexity: O(ALPHABET_SIZE * N * M)
- Where N is the number of words and M is the average length of words
- In practice, it's much less due to shared prefixes
