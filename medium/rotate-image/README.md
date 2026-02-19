# 48. Rotate Image

**Difficulty:** Medium

## Problem Description
Given an `n x n` 2D matrix representing an image, rotate it 90 degrees clockwise in-place. Do not allocate another matrix.

## Examples

### Example 1
```
Input:  [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

### Example 2
```
Input:  [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

## Constraints
- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Approach
Layer-by-layer in-place rotation using four-way swap:
1. Use `left/right` pointers to process one layer (ring) at a time, moving inward.
2. For each element `i` in the current layer, perform a 4-way cyclic swap:
   - Save `top-left` in `temp`.
   - `top-left` ← `bottom-left`
   - `bottom-left` ← `bottom-right`
   - `bottom-right` ← `top-right`
   - `top-right` ← `temp`
3. Advance `left` and retreat `right` after each layer.

## Time & Space Complexity
- **Time Complexity:** `O(n^2)` — every element is touched exactly once.
- **Space Complexity:** `O(1)` — only a single `temp` variable used.
