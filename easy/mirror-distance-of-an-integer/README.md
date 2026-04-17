# Mirror Distance of an Integer

Return abs(n - reverse(n)) where reverse(n) is n with its digits reversed.

## Approach
- Reverse the digits of n by repeatedly extracting the last digit (n % 10) and building the reversed number
- Return the absolute difference between the original and reversed values

Time Complexity: O(log n)
Space Complexity: O(1)
