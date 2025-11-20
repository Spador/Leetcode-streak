# 787. Cheapest Flights Within K Stops

**Difficulty:** Medium

## Problem Description
There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.

## Examples

### Example 1
```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation: The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
```

### Example 2
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
```

### Example 3
```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
```

## Constraints
- `2 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from_i, to_i < n`
- `from_i != to_i`
- `1 <= price_i <= 10^4`
- There will not be any multiple flights between two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## Approach
1. Use a modified Bellman-Ford algorithm that relaxes edges exactly `k + 1` times (allowing at most `k` stops means at most `k + 1` edges).
2. Initialize prices array with infinity for all cities except the source (set to 0).
3. For each iteration (up to `k + 1` times):
   - Create a temporary copy of current prices.
   - For each flight, if we can reach the source city, update the destination city's price in the temporary array.
   - Update the main prices array with the temporary values.
4. After all iterations, return the price to destination if it's not infinity, otherwise return `-1`.

## Algorithm
- Initialize `prices` array with `float("inf")` for all cities, except `prices[src] = 0`.
- For `i` in range `[0, k+1]`:
  - Create `temp_prices` as a copy of current `prices`.
  - For each flight `[s, d, p]`:
    - If `prices[s]` is not infinity, update `temp_prices[d] = min(temp_prices[d], prices[s] + p)`.
  - Set `prices = temp_prices`.
- Return `prices[dst]` if not infinity, else `-1`.

## Time & Space Complexity
- **Time Complexity:** `O(k * E)` where `E` is the number of flights, as we iterate `k+1` times and process all edges each time.
- **Space Complexity:** `O(n)` for the prices arrays.
