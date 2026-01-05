# 134. Gas Station

**Difficulty:** Medium

## Problem Description
There are `n` gas stations along a circular route, where the amount of gas at the `i`th station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i`th station to its next (`i + 1`)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`. If there exists a solution, it is guaranteed to be unique.

## Examples

### Example 1
```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```

### Example 2
```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```

## Constraints
- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`
- The input is generated such that the answer is unique.

## Approach
We can solve this using a greedy approach in `O(n)` time.

Observations:
- If the **total gas** is less than the **total cost**, it is impossible to complete the circuit from any starting point.
- If the total gas is at least the total cost, there is a **unique** valid starting index.

Greedy idea:
- Iterate once over all stations, maintaining a running balance `total` representing the current tank as we hypothetically start from some `start` index and move forward.
- For each station `i`, add `gas[i] - cost[i]` to `total`.
- If at any point `total` becomes negative, it means we cannot reach station `i + 1` from the current `start`. Therefore, any starting index between the previous `start` and `i` is also invalid.
  - Reset `total` to `0` and move `start` to `i + 1`.
- After finishing the loop, if `sum(gas) < sum(cost)`, return `-1` (no possible circuit). Otherwise, return `start`.

## Algorithm
1. If `sum(cost) > sum(gas)`, return `-1` immediately.
2. Initialize `total = 0`, `start = 0`.
3. For each index `i` from `0` to `n - 1`:
   - Update `total += gas[i] - cost[i]`.
   - If `total < 0`:
     - Set `total = 0`.
     - Set `start = i + 1` (next index becomes the new candidate start).
4. Return `start`.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(gas)`, since we traverse the arrays once.
- **Space Complexity:** `O(1)`, using only a few integer variables.

