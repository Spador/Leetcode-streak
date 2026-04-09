# Excel Sheet Column Title

Convert a column number to its Excel column title (1 → "A", 26 → "Z", 27 → "AA", etc.).

## Approach
- Decrement columnNumber by 1 to make it 0-indexed before each digit extraction
- Take remainder mod 26 to get the current letter, prepend to result
- Divide by 26 and repeat until columnNumber is 0

Time Complexity: O(log n)
Space Complexity: O(log n)
