# 17. Letter Combinations of a Phone Number

**Difficulty:** Medium

## Problem Description

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Examples

### Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2:
```
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints

- 1 <= digits.length <= 4
- digits[i] is a digit in the range ['2', '9'].

## Approach

This problem can be solved using backtracking:

1. **Digit to Letter Mapping**: Create a mapping from digits to their corresponding letters on a phone keypad.
2. **Backtracking Strategy**: For each digit, try all possible letters and recursively build combinations.
3. **Base Case**: When we've processed all digits, add the current combination to the result.
4. **Recursive Case**: For each letter corresponding to the current digit, add it to the current string and recursively process the next digit.

## Algorithm

1. Create a mapping from digits to letters
2. Handle edge case: if input is empty, return empty list
3. Use backtracking to generate all combinations:
   - Start with empty string and index 0
   - For each letter corresponding to current digit, add it to current string
   - Recursively process next digit
   - When all digits are processed, add current combination to result

## Time Complexity

- **Time**: O(4^n * n) where n is the length of digits
  - In the worst case, each digit can have 4 letters (7 and 9)
  - We generate 4^n combinations and each combination has length n
- **Space**: O(n) for the recursion stack

## Solution

The solution uses backtracking to generate all possible letter combinations by:
- Mapping each digit to its corresponding letters
- Recursively building combinations by trying each possible letter for each digit
- Adding complete combinations to the result when all digits are processed
