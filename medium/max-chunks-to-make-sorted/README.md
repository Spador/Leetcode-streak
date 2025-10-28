# 769. Max Chunks To Make Sorted

**Difficulty:** Medium

## Problem Description

You are given an integer array `arr` of length `n` that represents a permutation of the integers in the range `[0, n - 1]`.

We split `arr` into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

## Examples

### Example 1:
```
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
```

### Example 2:
```
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
```

## Constraints

- n == arr.length
- 1 <= n <= 10
- 0 <= arr[i] < n
- All the elements of arr are unique.

## Approach

This problem can be solved using a greedy approach with a single pass:

1. **Key Insight**: For a chunk to be valid, all elements in the chunk must be less than or equal to the maximum index we've seen so far
2. **Maximum Tracking**: Track the maximum value encountered up to current index
3. **Chunk Validation**: A chunk ending at index `i` is valid if the maximum value in that chunk equals `i`
4. **Greedy Splitting**: Count chunks whenever we can form a valid chunk

## Algorithm

1. Initialize `curr_max` to track maximum value seen so far
2. Initialize `result` to count number of chunks
3. Iterate through array:
   - Update `curr_max` with current element
   - If `curr_max == i` (current index), we can form a valid chunk ending here
   - Increment chunk count
4. Return the total number of chunks

## Implementation Details

- **Single Pass**: Process array in one iteration
- **Maximum Tracking**: Keep track of maximum value in current chunk
- **Index Comparison**: Compare maximum with current index to validate chunk
- **Greedy Approach**: Form chunks as early as possible

## Key Optimizations

- **O(n) Time**: Single pass through the array
- **O(1) Space**: Only use constant extra space
- **Greedy Strategy**: Optimal solution without backtracking

## Time Complexity

- **Time**: O(n) where n is the length of the array
  - Single pass through the array
- **Space**: O(1) for tracking maximum and result

## Solution

The solution uses a greedy approach:
- Tracks maximum value encountered so far
- Forms chunks when maximum equals current index
- Returns the maximum number of valid chunks possible
