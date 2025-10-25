from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Initialize parent array where each node is its own parent
        parent = [i for i in range(n)]
        # Initialize rank array for union by rank optimization
        rank = [1] * n
        
        def find(n1):
            """Find root with path compression optimization"""
            p = parent[n1]
            while p != parent[p]:
                # Path compression: make every node point directly to root
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            """Union two components with union by rank optimization"""
            p1, p2 = find(n1), find(n2)
            
            # If already in same component, adding edge creates a cycle
            if p1 == p2:
                return False
            
            # Union by rank: attach smaller tree to larger tree
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True  # Return True to indicate successful union
        
        # Process all edges
        for n1, n2 in edges:
            # If union returns False, edge creates a cycle
            if union(n1, n2) == False:
                return False
            # Decrease component count when two components are merged
            n -= 1
        
        # Valid tree must have exactly 1 component (connected)
        return True if n == 1 else False
