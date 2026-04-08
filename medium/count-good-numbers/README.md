# Count Good Numbers

Return the total number of good digit strings of length n, where even indices hold even digits (5 choices) and odd indices hold prime digits (4 choices).

## Approach
- Even-indexed positions: ceil(n/2) positions, each with 5 choices
- Odd-indexed positions: floor(n/2) positions, each with 4 choices
- Use fast modular exponentiation to compute 5^even * 4^odd mod (10^9 + 7)

Time Complexity: O(log n)
Space Complexity: O(1)
