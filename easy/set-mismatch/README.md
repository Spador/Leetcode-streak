# Set Mismatch

Find the number that appears twice and the number that is missing from an array that should contain 1 to n.

## Approach
- Use the array itself as a visited marker by negating nums[abs(n) - 1] for each n
- If the value at that index is already negative, abs(n) is the duplicate
- In a second pass, the index whose value is still positive (and isn't the duplicate) gives the missing number

Time Complexity: O(n)
Space Complexity: O(1)
