# Valid Word Abbreviation

Check if a word abbreviation is valid according to given rules.

## Approach
- Use two pointers to track positions in word and abbreviation
- For digits in abbreviation:
  - Check for leading zeros
  - Parse complete number
  - Skip corresponding characters in word
- For letters:
  - Compare characters directly
  - Move both pointers forward
- Verify both strings are fully processed

Time Complexity: O(n)
Space Complexity: O(1) 