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

This problem can be solved using Depth-First Search (DFS) with backtracking:

1. **Graph Construction**: Build adjacency list from tickets, sorted for lexical order
2. **DFS with Backtracking**: Explore all possible paths starting from "JFK"
3. **Lexical Order**: Process destinations in sorted order to ensure smallest lexical result
4. **Ticket Usage**: Use each ticket exactly once (remove from adjacency list when used)

## Algorithm

1. Build adjacency list from tickets, sorting destinations for lexical order
2. Start DFS from "JFK" with result path initialized
3. For each current airport:
   - If all tickets used (path length = tickets.length + 1), return true
   - Try each destination in lexical order
   - Remove ticket from adjacency list (use ticket)
   - Add destination to result path
   - Recursively explore from destination
   - If successful, return true
   - Otherwise, backtrack: restore ticket and remove from path
4. Return the reconstructed itinerary

## Implementation Details

- **Sorted Adjacency List**: Process destinations in lexical order
- **Backtracking**: Remove and restore tickets during DFS exploration
- **Path Tracking**: Maintain result path throughout DFS
- **Early Termination**: Return immediately when valid itinerary found

## Key Optimizations

- **Lexical Sorting**: Sort destinations to ensure smallest lexical order
- **Backtracking**: Efficiently explore all possibilities with ticket restoration
- **Early Return**: Stop as soon as valid itinerary is found

## Time Complexity

- **Time**: O(E^E) where E is number of tickets
  - In worst case, we explore all possible paths
- **Space**: O(E) for the adjacency list and recursion stack

## Solution

The solution uses DFS with backtracking:
- Builds sorted adjacency list from tickets
- Explores paths starting from "JFK" in lexical order
- Uses backtracking to try all possible itineraries
- Returns the lexicographically smallest valid itinerary
