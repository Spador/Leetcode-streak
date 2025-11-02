# 2259. Remove Digit From Number to Maximize Result

**Difficulty:** Easy

## Problem Description

You are given a string `number` representing a positive integer and a character `digit`.

Return the resulting string after removing exactly one occurrence of `digit` from `number` such that the value of the resulting string in decimal form is maximized. The test cases are generated such that `digit` occurs at least once in `number`.

## Examples

### Example 1:
```
Input: number = "123", digit = "3"
Output: "12"
Explanation: There is only one '3' in "123". After removing '3', the result is "12".
```

### Example 2:
```
Input: number = "1231", digit = "1"
Output: "231"
Explanation: We can remove the first '1' to get "231" or remove the second '1' to get "123".
Since 231 > 123, we return "231".
```

### Example 3:
```
Input: number = "551", digit = "5"
Output: "51"
Explanation: We can remove either the first or second '5' from "551".
Both result in the string "51".
```

## Constraints

- 2 <= number.length <= 100
- number consists of digits from '1' to '9'.
- digit is a digit from '1' to '9'.
- digit occurs at least once in number.

## Approach

This problem can be solved by trying all possible removals:

1. **Brute Force**: Try removing each occurrence of the digit
2. **Comparison**: Compare all resulting strings
3. **Maximization**: Return the string with maximum value

## Algorithm

1. Initialize result as empty string
2. Iterate through each index in number:
   - If character at index matches digit:
     - Create candidate by removing that character
     - If candidate > result, update result
3. Return the maximum result

## Implementation Details

- **String Slicing**: Remove character at each position
- **String Comparison**: Compare strings lexicographically (works for numeric strings)
- **Greedy Approach**: Try all possibilities and pick maximum

## Key Optimizations

- **O(n²) Time**: n positions × n string operations
- **Simple Logic**: Straightforward brute force approach
- **String Comparison**: Leverages lexicographic comparison

## Time Complexity

- **Time**: O(n²) where n is the length of number
  - For each occurrence, create new string (O(n))
- **Space**: O(n) for the result string

## Solution

The solution tries all possible removals:
- Removes each occurrence of digit
- Compares resulting strings
- Returns the maximum value string
