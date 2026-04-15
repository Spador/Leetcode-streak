# Count Odd Numbers in an Interval Range

Return the count of odd numbers between low and high inclusive.

## Approach
- If either low or high is odd, the range includes one extra odd number compared to a fully even-bounded range
- Return (high - low) // 2 + 1 if either endpoint is odd, else (high - low) // 2

Time Complexity: O(1)
Space Complexity: O(1)
