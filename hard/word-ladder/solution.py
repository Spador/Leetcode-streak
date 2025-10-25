from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Check if endWord exists in wordList
        if endWord not in wordList:
            return 0
        
        # Build adjacency list using pattern matching
        connections = defaultdict(list)
        wordList.append(beginWord)  # Add beginWord to wordList for pattern matching
        
        # Create patterns for each word
        for word in wordList:
            for j in range(len(word)):
                # Create pattern by replacing character at position j with '*'
                pattern = word[:j] + "*" + word[j + 1:]
                connections[pattern].append(word)
        
        # Perform BFS to find shortest path
        visited = set([beginWord])
        q = deque([beginWord])
        result = 1  # Start with 1 since beginWord counts as first word
        
        while q:
            # Process all words at current level
            for i in range(len(q)):
                word = q.popleft()
                
                # If we reached endWord, return transformation count
                if word == endWord:
                    return result
                
                # Generate all possible patterns for current word
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    
                    # Add all unvisited words that match this pattern
                    for nextWord in connections[pattern]:
                        if nextWord not in visited:
                            visited.add(nextWord)
                            q.append(nextWord)
            
            # Increment transformation count after processing each level
            result += 1
        
        return 0  # No path found
