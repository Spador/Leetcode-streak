# 128. Longest Consecutive Sequence

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## Examples

### Example 1:
```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

### Example 2:
```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

### Example 3:
```
Input: nums = [1,0,1,2]
Output: 3
```

## Constraints

- `0 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

## Approach

The solution uses a hash set to achieve O(n) time complexity:

1. Convert the array to a set for O(1) lookups
2. For each number, check if it's the start of a consecutive sequence (i.e., `n-1` is not in the set)
3. If it is the start, count how many consecutive numbers follow it
4. Keep track of the maximum length found
5. Early termination optimization: if the current longest sequence is greater than half the array length, return it immediately

## Time Complexity

O(n) - Each number is visited at most twice (once in the outer loop, once in the inner while loop).

## Space Complexity

O(n) for storing the hash set.
