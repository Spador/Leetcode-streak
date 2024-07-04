# Roman to Integer

Convert a Roman numeral to an integer.

## Approach
- Use hashmap to store Roman numeral values
- Track previous value to handle subtraction cases
- Subtract twice the previous value when current > previous
- Add current value to result

Time Complexity: O(n)
Space Complexity: O(1) 