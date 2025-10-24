from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent array where each node is its own parent
        parent = [i for i in range(len(edges) + 1)]
        # Initialize rank array for union by rank optimization
        rank = [1] * len(parent)
        
        def find(n):
            """Find root with path compression optimization"""
            p = parent[n]
            while p != parent[p]:
                # Path compression: make every node point directly to root
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            """Union two components with union by rank optimization"""
            p1, p2 = find(n1), find(n2)
            
            # If already in same component, adding edge creates cycle
            if p1 == p2:
                return False
            
            # Union by rank: attach smaller tree to larger tree
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        # Process edges in order
        for n1, n2 in edges:
            # If union returns False, this edge creates a cycle (redundant)
            if not union(n1, n2):
                return [n1, n2]
