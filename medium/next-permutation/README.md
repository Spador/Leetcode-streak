# 31. Next Permutation

**Difficulty:** Medium

## Problem Description
Given an array of integers `nums`, rearrange it in-place to its next lexicographically greater permutation. If no such permutation exists (array is descending), rearrange to the lowest order (ascending). Must use constant extra memory.

## Examples

### Example 1
```
Input: nums = [1,2,3]
Output: [1,3,2]
```

### Example 2
```
Input: nums = [3,2,1]
Output: [1,2,3]
```

### Example 3
```
Input: nums = [1,1,5]
Output: [1,5,1]
```

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Approach
1. Scan from the right to find the first index `rev` where the order breaks (i.e., `nums[rev] < nums[rev+1]`).
2. Reverse the suffix starting at `rev+1` — this makes the suffix ascending (smallest order).
3. If `rev == -1`, the whole array was descending; the reverse already gives the smallest permutation, so return.
4. Otherwise, scan the (now sorted) suffix to find the first element greater than `nums[rev]`, and swap them.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — at most two linear scans and one reverse.
- **Space Complexity:** `O(1)` — all operations done in-place.
