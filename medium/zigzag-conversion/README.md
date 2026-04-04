# Zigzag Conversion

Write a string in zigzag pattern across numRows rows, then read it row by row.

## Approach
- The cycle length for each row is 2 * (numRows - 1)
- For each row r, characters appear at indices r, r + cycle, r + 2*cycle, ...
- For middle rows (not first or last), there is an additional diagonal character between main characters at index i + cycle - 2*r
- Concatenate characters row by row to build the result

Time Complexity: O(n)
Space Complexity: O(n)
