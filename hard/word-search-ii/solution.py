# spador

# Making a Trie (Prefix Tree) to store all the words
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # store all the words
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])
        
        # result stores all the words found
        # visit stores all the cells already visited in an iteration
        result, visit = set(), set()

        # dfs backtracking to traverse the matrix
        def dfs(r, c, node, word):
            if r < 0 or r == rows or c < 0 or c == cols or board[r][c] not in node.children or (r, c) in visit:
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                result.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))
        
        # run dfs for each word
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(result)
