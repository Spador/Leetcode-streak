# 875. Koko Eating Bananas

**Difficulty:** Medium

## Problem Description
Given `n` piles of bananas and `h` hours, find the minimum eating speed `k` such that Koko can eat all bananas within `h` hours (she eats at most `k` bananas per pile per hour).

## Examples

### Example 1
```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

### Example 2
```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

### Example 3
```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## Constraints
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Approach
Binary search on the answer space `[1, max(piles)]`:
1. For each candidate speed `k`, compute total hours needed using `ceil(p / k)` for each pile.
2. If hours <= `h`, it's a valid speed — try smaller (move right left).
3. Otherwise try larger (move left right).
4. Track the minimum valid `k` found.

## Time & Space Complexity
- **Time Complexity:** `O(n log m)` where `m = max(piles)`
- **Space Complexity:** `O(1)`
