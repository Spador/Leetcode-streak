from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build adjacency list from tickets
        adjList = {src: [] for src, dst in tickets}
        
        # Sort tickets to ensure lexical order
        tickets.sort()
        
        # Populate adjacency list
        for src, dst in tickets:
            adjList[src].append(dst)
        
        # Initialize result path starting with JFK
        result = ["JFK"]
        
        def dfs(src):
            """DFS with backtracking to find valid itinerary"""
            # If we've used all tickets, we found a valid itinerary
            if len(result) == len(tickets) + 1:
                return True
            
            # If current airport has no outgoing flights, backtrack
            if src not in adjList:
                return False
            
            # Try each destination in lexical order
            temp = list(adjList[src])  # Create copy to iterate safely
            for i, destination in enumerate(temp):
                # Remove ticket from adjacency list (use the ticket)
                adjList[src].pop(i)
                result.append(destination)
                
                # Recursively explore from destination
                if dfs(destination):
                    return True
                
                # Backtrack: restore ticket and remove from path
                adjList[src].insert(i, destination)
                result.pop()
            
            return False
        
        # Start DFS from JFK
        dfs("JFK")
        return result
