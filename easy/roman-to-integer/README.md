# 13. Roman to Integer

**Difficulty:** Easy

## Problem Description

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

## Examples

### Example 1:
```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

### Example 2:
```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

### Example 3:
```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

## Constraints

- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].

## Approach

This problem can be solved using a single pass through the string:

1. **HashMap Lookup**: Create a mapping of Roman symbols to their integer values
2. **Subtraction Rule**: When a smaller value appears before a larger value, subtract it
3. **Addition Rule**: Otherwise, add the value to the result
4. **Single Pass**: Process the string from left to right

## Algorithm

1. Create a hashmap mapping Roman symbols to their values
2. Initialize result to 0
3. For each character in the string:
   - If current value is less than next value, subtract current value
   - Otherwise, add current value to result
4. Return the final result

## Implementation Details

- **Look-ahead Comparison**: Compare current character with next character
- **Subtraction Handling**: Subtract when smaller value precedes larger value
- **Addition Handling**: Add when value should be added normally

## Key Optimizations

- **Single Pass**: Process string in one iteration
- **O(1) Lookup**: HashMap provides constant time symbol lookup
- **Simple Logic**: Straightforward comparison-based approach

## Time Complexity

- **Time**: O(n) where n is the length of the string
  - Single pass through the string
- **Space**: O(1) for the hashmap (fixed size)

## Solution

The solution uses a hashmap and look-ahead comparison:
- Maps Roman symbols to their integer values
- Subtracts when smaller value precedes larger value
- Adds otherwise
- Returns the converted integer value