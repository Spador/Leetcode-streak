# 496. Next Greater Element I

**Difficulty:** Easy

## Problem Description
The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

## Examples

### Example 1
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
```

### Example 2
```
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```

## Constraints
- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are unique.
- All the integers of `nums1` also appear in `nums2`.

## Approach
We first map each value in `nums1` to its index in `nums1` so we can quickly place answers into the correct positions.

### Naive (O(m * n)) approach
For each element in `nums2` that appears in `nums1`:
- Scan to the right in `nums2` to find the first element that is greater; if found, write it into the corresponding position in `result`, otherwise leave it as `-1`.

### Optimized (follow-up) O(n + m) idea
A more optimal solution uses a **monotonic stack** over `nums2` to precompute next greater values, but in the provided code, that logic is sketched after an early `return` of the naive solution.

## Time & Space Complexity (for the implemented part)
- **Time Complexity:** `O(m * n)` in the worst case, where `m = len(nums1)` and `n = len(nums2)` (nested scan).
- **Space Complexity:** `O(m)` for the `result` array and the hash map from value to index.
