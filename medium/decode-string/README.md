# 394. Decode String

**Difficulty:** Medium

## Problem Description

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed 10⁵.

## Examples

### Example 1:
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

### Example 2:
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

### Example 3:
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints

- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and square brackets '[]'.
- s is guaranteed to be a valid input.
- All the integers in s are in the range [1, 300].

## Approach

This problem can be solved using a stack-based approach:

1. **Stack Processing**: Use a stack to process characters and nested structures
2. **Character Accumulation**: When encountering ']', extract the substring and repeat count
3. **Nested Handling**: Stack naturally handles nested brackets
4. **String Building**: Build decoded string by processing from innermost to outermost

## Algorithm

1. Initialize an empty stack
2. Iterate through each character in the string:
   - If character is not ']', push it to stack
   - If character is ']':
     - Pop characters until '[' is found (this is the encoded substring)
     - Pop '[' from stack
     - Pop digits to get the repeat count k
     - Push k * substring back to stack
3. Join all elements in stack to form the final decoded string

## Implementation Details

- **Stack-based Processing**: Use stack to handle nested brackets naturally
- **Reverse String Building**: Extract substring by popping until '['
- **Number Extraction**: Extract multi-digit numbers by popping digits
- **String Repetition**: Multiply substring by count and push back

## Key Optimizations

- **Single Pass**: Process string in one pass
- **Stack Efficiency**: Stack handles nested structures automatically
- **In-place Processing**: Build result directly in stack

## Time Complexity

- **Time**: O(n × m) where n is string length and m is maximum repeat count
  - We process each character and may repeat substrings
- **Space**: O(n) for the stack in worst case

## Solution

The solution uses a stack-based approach:
- Processes characters and pushes to stack
- When encountering ']', extracts substring and repeat count
- Handles nested brackets naturally through stack operations
- Returns the fully decoded string
