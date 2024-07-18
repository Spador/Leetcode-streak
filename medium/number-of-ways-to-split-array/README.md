# Number of Ways to Split Array

Count the number of valid ways to split an array so that the sum of the left part is greater than or equal to the sum of the right part.

## Approach
- Calculate total sum of the array
- Iterate through the array, maintaining a prefix sum
- For each split point, compare prefix sum with remaining sum
- Increment count if prefix sum is greater than or equal to right sum

Time Complexity: O(n)
Space Complexity: O(1) 