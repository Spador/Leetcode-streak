from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)
        
        def backtrack(node_id, path):
            # If we reached the target node, add current path to result
            if node_id == n - 1:
                result.append(path + [node_id])
                return
            
            # Explore all neighbors of current node
            for neighbor in graph[node_id]:
                # Recursively backtrack with updated path
                backtrack(neighbor, path + [node_id])
        
        # Start backtracking from node 0 with empty path
        backtrack(0, [])
        return result
