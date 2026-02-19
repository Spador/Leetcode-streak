# 799. Champagne Tower

**Difficulty:** Medium

## Problem Description
Glasses are stacked in a pyramid where row `i` has `i+1` glasses. Champagne is poured into the top glass. When a glass overflows, the excess splits equally to the two glasses below. Return how full the `j`th glass in the `i`th row is (0-indexed).

## Examples

### Example 1
```
Input: poured = 1, query_row = 1, query_glass = 1
Output: 0.00000
```

### Example 2
```
Input: poured = 2, query_row = 1, query_glass = 1
Output: 0.50000
```

### Example 3
```
Input: poured = 100000009, query_row = 33, query_glass = 17
Output: 1.00000
```

## Constraints
- `0 <= poured <= 10^9`
- `0 <= query_glass <= query_row < 100`

## Approach
Row-by-row simulation with space optimisation:
1. Start with `prev_row = [poured]`.
2. For each row up to `query_row`, compute `curr_row` by distributing overflow from each glass in `prev_row` — if a glass holds more than 1 cup, the excess (`val - 1`) splits 50/50 to the two glasses below.
3. Only keep the previous row in memory at any time.
4. Return `min(1, prev_row[query_glass])` — a glass can never be more than full.

## Time & Space Complexity
- **Time Complexity:** `O(query_row^2)` — fills each row up to `query_row`.
- **Space Complexity:** `O(query_row)` — only two rows stored at a time.
