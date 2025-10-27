from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build graph from tickets
        graph = {}
        
        # Sort tickets by destination to ensure lexical order
        tickets.sort(key=lambda x: x[1])

        # Populate graph
        for u, v in tickets:
            if u in graph:
                graph[u].append(v)
            else:
                graph[u] = [v]
        
        # Use iterative DFS with stack
        itinerary, stack = [], [("JFK")]
        
        while stack:
            curr = stack[-1]
            
            # If current airport has outgoing flights, add next destination to stack
            if curr in graph and len(graph[curr]) > 0:
                stack.append(graph[curr].pop(0))
            else:
                # No more outgoing flights, add current airport to itinerary
                itinerary.append(stack.pop())
        
        # Reverse to get correct order
        return itinerary[::-1]