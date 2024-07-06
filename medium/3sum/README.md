# 3Sum

Find all unique triplets in the array which gives the sum of zero.

## Approach
- Sort array to handle duplicates
- For each number, solve as 2Sum II problem
- Use two pointers to find pairs that sum to complement
- Skip duplicates to avoid repeated triplets

Time Complexity: O(n²)
Space Complexity: O(1) 