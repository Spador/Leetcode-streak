# 4. Median of Two Sorted Arrays

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

## Examples

### Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

### Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Approach

The solution uses **binary search** to find the correct partition:

1. **Ensure A is the smaller array**: If `nums2` is smaller than `nums1`, swap them
2. **Binary Search on A**: Search for the correct partition point in the smaller array
3. **Calculate B's partition**: `j = mid - i - 2` where `mid = total // 2`
4. **Check partition validity**: 
   - `Aleft <= Bright` and `Bleft <= Aright`
   - If valid, we found the correct partition
   - If not, adjust the search range
5. **Return median**:
   - For odd total: `min(Aright, Bright)`
   - For even total: `(max(Aleft, Bleft) + min(Aright, Bright)) / 2`

**Key Insight**: The median divides the merged array into two equal halves, so we can find the correct partition using binary search.

## Time Complexity

O(log(min(m, n))) - Binary search on the smaller array.

## Space Complexity

O(1) - Only using a constant amount of extra space.
