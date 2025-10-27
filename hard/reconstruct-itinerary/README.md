# 332. Reconstruct Itinerary

**Difficulty:** Hard

## Problem Description

You are given a list of airline tickets where `tickets[i] = [fromi, toi]` represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary `["JFK", "LGA"]` has a smaller lexical order than `["JFK", "LGB"]`.

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

## Examples

### Example 1:
```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

### Example 2:
```
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
```

## Constraints

- 1 <= tickets.length <= 300
- tickets[i].length == 2
- fromi.length == 3
- toi.length == 3
- fromi and toi consist of uppercase English letters.
- fromi != toi

## Approach

This problem can be solved using an iterative Depth-First Search (DFS) approach with a stack:

1. **Graph Construction**: Build adjacency list from tickets, sorted by destination for lexical order
2. **Iterative DFS**: Use a stack to simulate DFS traversal without recursion
3. **Eulerian Path**: This is essentially finding an Eulerian path in the graph
4. **Lexical Order**: Sort destinations to ensure smallest lexical order result

## Algorithm

1. Build graph from tickets, sorting by destination to ensure lexical order
2. Initialize stack with "JFK" and empty itinerary
3. While stack is not empty:
   - Get current airport from top of stack
   - If current airport has outgoing flights:
     - Add the lexicographically smallest destination to stack
     - Remove that destination from the airport's outgoing flights
   - If no outgoing flights:
     - Add current airport to itinerary
     - Remove airport from stack
4. Reverse itinerary to get correct order

## Implementation Details

- **Iterative Approach**: Uses stack instead of recursion for better performance
- **Lexical Sorting**: Sort tickets by destination to ensure lexical order
- **Stack-based DFS**: Simulates DFS traversal using explicit stack
- **Post-order Processing**: Add airports to result when no more outgoing flights

## Key Optimizations

- **Iterative DFS**: Avoids recursion overhead and stack overflow
- **Lexical Sorting**: Ensures smallest lexical order without backtracking
- **Eulerian Path**: Leverages mathematical property for efficient solution
- **Stack Simulation**: More memory efficient than recursive approach

## Time Complexity

- **Time**: O(E log E) where E is number of tickets
  - Sorting tickets: O(E log E)
  - DFS traversal: O(E)
- **Space**: O(E) for the graph and stack

## Solution

The solution uses iterative DFS with stack:
- Builds graph from tickets sorted by destination
- Uses stack-based DFS to find Eulerian path
- Processes airports in post-order for correct itinerary
- Returns lexicographically smallest valid itinerary
