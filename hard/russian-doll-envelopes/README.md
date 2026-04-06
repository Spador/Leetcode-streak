# Russian Doll Envelopes

Return the maximum number of envelopes that can be nested inside each other (both width and height must be strictly greater).

## Approach
- Sort envelopes by width ascending; for ties in width sort by height descending (prevents using two same-width envelopes in the same sequence)
- Run LIS (Longest Increasing Subsequence) on heights using binary search (patience sorting)
- Maintain a dp array where dp[i] is the smallest tail element for an increasing subsequence of length i+1
- For each height, binary search for its position and replace or extend dp

Time Complexity: O(n log n)
Space Complexity: O(n)
