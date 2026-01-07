# 1296. Divide Array in Sets of K Consecutive Numbers

**Difficulty:** Medium

## Problem Description
Given an array of integers `nums` and a positive integer `k`, check whether it is possible to divide this array into sets of `k` consecutive numbers.

Return `true` if it is possible. Otherwise, return `false`.

## Examples

### Example 1
```
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
```

### Example 2
```
Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
```

### Example 3
```
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
```

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`

> Note: This question is the same as 846: Hand of Straights.

## Approach
This problem is equivalent to checking if we can partition the multiset of numbers into groups of size `k` where each group consists of `k` **consecutive** integers.

We can reuse the same greedy + heap strategy as in "Hand of Straights":

1. If `len(nums) % k != 0`, it's impossible to divide all numbers into equal-sized groups, so return `False`.
2. Build a frequency map `count` of all numbers in `nums`.
3. Put all distinct keys of `count` into a **min-heap** so that we can always start forming groups from the smallest available number.
4. While the heap is not empty:
   - Let `first` be the current smallest number (`minH[0]`).
   - Try to form a consecutive group `[first, first + 1, ..., first + k - 1]`.
   - For each `i` from `first` to `first + k - 1`:
     - If `i` is not in `count`, then we cannot form a complete group, so return `False`.
     - Decrement `count[i]` by 1.
     - If `count[i]` becomes `0`, then:
       - It must be the current smallest element in the heap (`i == minH[0]`); otherwise, the ordering is broken, so return `False`.
       - Pop it from the heap.
5. If we successfully consume all counts following these rules, return `True`.

This ensures that:
- We always form groups starting from the smallest remaining number.
- We enforce consecutiveness and correct multiplicities using the frequency map and heap order.

## Time & Space Complexity
- **Time Complexity:** `O(n log n)` where `n = len(nums)`:
  - Building the heap is `O(m)`, where `m` is the number of distinct values (`m <= n`).
  - Each element is processed once, with heap operations costing up to `O(log m)` each.
- **Space Complexity:** `O(m)` for the frequency map and heap.

