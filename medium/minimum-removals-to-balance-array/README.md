# 3634. Minimum Removals to Balance Array

**Difficulty:** Medium

## Problem Description
You are given an integer array `nums` and an integer `k`.

An array is considered **balanced** if the value of its maximum element is at most `k` times the minimum element.

You may remove any number of elements from `nums` without making it empty.

Return the **minimum number of elements to remove** so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

## Examples

### Example 1
```
Input: nums = [2,1,5], k = 2
Output: 1
Explanation:
Remove nums[2] = 5 to get nums = [2, 1].
Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.
```

### Example 2
```
Input: nums = [1,6,2,9], k = 3
Output: 2
Explanation:
Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.
```

### Example 3
```
Input: nums = [4,6], k = 2
Output: 0
Explanation:
Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.
```

## Constraints
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= 10^5`

## Approach
We want to keep a **maximal balanced subarray** after sorting, then remove everything outside it.

1. Sort `nums` in non-decreasing order.
2. Use two pointers (`left` and `right`) to find the longest window `[left, right)` such that:
   - `nums[right - 1] <= nums[left] * k`
3. For each `left` from `0` to `n - 1`:
   - Compute `mval = nums[left] * k`.
   - Move `right` forward while `right < n` and `nums[right] <= mval`.
   - The window size is `right - left`; the number of elements to **keep** is this size.
   - The number of removals if we choose this window is `n - (right - left)`.
   - Track the minimum removals over all `left` positions.
4. Return this minimum value.

Because the array is sorted, the minimum of any chosen subarray is at `left` and the maximum is at `right - 1`, so checking `nums[right - 1] <= nums[left] * k` ensures the subarray is balanced.

## Time & Space Complexity
- **Time Complexity:** `O(n log n + n)` due to sorting (`O(n log n)`) and a single linear pass with two pointers (`O(n)`).
- **Space Complexity:** `O(1)` extra space (ignoring the space used by the sort, which can be in-place).
