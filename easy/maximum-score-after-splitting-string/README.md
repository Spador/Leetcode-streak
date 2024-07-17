# Maximum Score After Splitting a String

Find maximum score by splitting a binary string into two parts.

## Approach
- Use prefix sum to count zeros efficiently
- For each possible split point:
  - Count zeros in left part using prefix sum
  - Calculate ones in right part using total length and zero counts
  - Update maximum score if current split gives better result

Time Complexity: O(n)
Space Complexity: O(n) 