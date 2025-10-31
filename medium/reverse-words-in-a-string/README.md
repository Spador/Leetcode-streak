# 151. Reverse Words in a String

**Difficulty:** Medium

## Problem Description

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

## Examples

### Example 1:
```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

### Example 2:
```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

### Example 3:
```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

## Constraints

- 1 <= s.length <= 10⁴
- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
- There is at least one word in s.

## Follow-up

If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

## Approach

This problem can be solved using string processing:

1. **Word Extraction**: Extract words from the string, handling multiple spaces
2. **Word Collection**: Collect words in order while skipping empty strings
3. **Reversal**: Reverse the order of collected words
4. **Joining**: Join words with single spaces

## Algorithm

1. Initialize a list to store words and a temporary word string
2. Add a trailing space to handle the last word
3. Iterate through each character:
   - If character is not space, append to current word
   - If character is space and word is not empty, add word to list and reset word
4. Reverse the list of words and join with single space

## Implementation Details

- **Word Building**: Build words character by character
- **Space Handling**: Skip multiple consecutive spaces
- **List Reversal**: Reverse the collected words list
- **String Joining**: Join words with single space separator

## Key Optimizations

- **Single Pass**: Process string in one iteration
- **Efficient Storage**: Store only words, not spaces
- **Clean Output**: Automatically handles multiple spaces

## Time Complexity

- **Time**: O(n) where n is the length of the string
  - Single pass through the string
  - Reversal and joining operations
- **Space**: O(n) for storing words

## Solution

The solution uses string processing:
- Extracts words while handling multiple spaces
- Collects words in a list
- Reverses the list and joins with single space
- Returns the reversed words string
