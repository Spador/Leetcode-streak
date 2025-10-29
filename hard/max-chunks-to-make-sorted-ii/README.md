# 768. Max Chunks To Make Sorted II

**Difficulty:** Hard

## Problem Description

You are given an integer array `arr`.

We split `arr` into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

## Examples

### Example 1:
```
Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
```

### Example 2:
```
Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
```

## Constraints

- 1 <= arr.length <= 2000
- 0 <= arr[i] <= 10⁸

## Approach

This problem can be solved using a stack-based approach:

1. **Stack for Chunks**: Use a stack to maintain the maximum value of each chunk
2. **Merging Logic**: When encountering a smaller value, merge chunks until the condition is satisfied
3. **Chunk Validation**: Each chunk's maximum must be less than or equal to all values in subsequent chunks
4. **Greedy Strategy**: Form chunks greedily while maintaining the sorted property

## Algorithm

1. Initialize an empty stack
2. For each number in the array:
   - Set current maximum to the current number
   - While stack is not empty and current number is less than top of stack:
     - Pop from stack and update current maximum
   - Push the maximum value to stack
3. Return the length of the stack (number of chunks)

## Implementation Details

- **Stack-based Processing**: Use stack to track chunk maximums
- **Merging Chunks**: Merge chunks when smaller value is encountered
- **Maximum Tracking**: Keep track of maximum value in merged chunks
- **Greedy Approach**: Form chunks as early as possible

## Key Optimizations

- **Stack Efficiency**: O(n) time complexity with stack operations
- **Single Pass**: Process array in one iteration
- **Merging Strategy**: Merge chunks only when necessary

## Time Complexity

- **Time**: O(n) where n is the length of the array
  - Each element is pushed and popped at most once
- **Space**: O(n) for the stack in worst case

## Solution

The solution uses a stack-based approach:
- Maintains chunk maximums in a stack
- Merges chunks when smaller values are encountered
- Returns the maximum number of valid chunks
