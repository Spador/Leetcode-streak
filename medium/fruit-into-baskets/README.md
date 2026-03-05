# 904. Fruit Into Baskets

**Difficulty:** Medium

## Problem Description
Given an array `fruits` representing fruit types on trees, pick the maximum number of fruits using only two baskets (each holds one fruit type), picking from a contiguous subarray.

## Examples

### Example 1
```
Input: fruits = [1,2,1]
Output: 3
```

### Example 2
```
Input: fruits = [0,1,2,2]
Output: 3
```

### Example 3
```
Input: fruits = [1,2,3,2,2]
Output: 4
```

## Constraints
- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`

## Approach
Sliding window with a frequency map: expand `right`, shrink from `left` when more than 2 distinct fruit types are in the window. Track max window size.

## Time & Space Complexity
- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)` — at most 3 keys in the map at any time
