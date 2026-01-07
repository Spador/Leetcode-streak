# 1899. Merge Triplets to Form Target Triplet

**Difficulty:** Medium

## Problem Description
A triplet is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [a_i, b_i, c_i]` describes the `i`th triplet. You are also given an integer array `target = [x, y, z]` that describes the triplet you want to obtain.

To obtain `target`, you may apply the following operation on `triplets` any number of times (possibly zero):

- Choose two indices (0-indexed) `i` and `j` (`i != j`) and update `triplets[j]` to become:
  - `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.

For example, if `triplets[i] = [2, 5, 3]` and `triplets[j] = [1, 7, 5]`, `triplets[j]` will be updated to:

`[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]`.

Return `true` if it is possible to obtain the target triplet `[x, y, z]` as an element of `triplets`, or `false` otherwise.

## Examples

### Example 1
```
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. 
  Update the last triplet to be [max(2,1), max(5,7), max(3,5)] = [2,7,5]. 
  triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.
```

### Example 2
```
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.
```

### Example 3
```
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. 
  Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. 
  triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. 
  Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. 
  triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
```

## Constraints
- `1 <= triplets.length <= 10^5`
- `triplets[i].length == target.length == 3`
- `1 <= a_i, b_i, c_i, x, y, z <= 1000`

## Approach
Key idea: We only care about triplets that are **component-wise less than or equal to** the target, because:
- If any component of a triplet is **greater** than the corresponding target component, that triplet can never help form the exact target (max operations will keep that component too large).

Algorithm:
1. Initialize an empty set `good` to track which indices (0, 1, 2) of the target have been "matched" exactly by some valid triplets.
2. Iterate over each `triplet` in `triplets`:
   - If any component `triplet[i]` is greater than `target[i]` for some `i`, skip this triplet (it is invalid).
   - Otherwise, for each index `i` in `{0, 1, 2}`:
     - If `triplet[i] == target[i]`, add `i` to `good`.
   - If `good` contains all three indices `{0, 1, 2}`, then we can combine such triplets via the max operations to form the exact `target`, so return `True`.
3. If the loop finishes and `good` does not contain all three indices, return `False`.

Why this works:
- The max operation is monotonic and component-wise independent. As long as we have:
  - At least one valid triplet with `a_i == x`,
  - At least one (possibly different) valid triplet with `b_i == y`,
  - At least one valid triplet with `c_i == z`,
  and none of these triplets exceed the target component-wise,
  we can combine them to construct `[x, y, z]`.

## Time & Space Complexity
- **Time Complexity:** `O(n)`, where `n = len(triplets)`, since we scan the list once and do `O(1)` work per triplet.
- **Space Complexity:** `O(1)`, using a small set and a few variables.

