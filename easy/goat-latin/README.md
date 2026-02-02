# 824. Goat Latin

**Difficulty:** Easy

## Problem Description
You are given a string `sentence` that consists of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin). The rules of Goat Latin are as follows:

1. If a word begins with a vowel (`'a'`, `'e'`, `'i'`, `'o'`, or `'u'`, case-insensitive), append `"ma"` to the end of the word.
   - Example: `"apple"` becomes `"applema"`.
2. If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add `"ma"`.
   - Example: `"goat"` becomes `"oatgma"`.
3. Add one letter `'a'` to the end of each word per its word index in the sentence, starting with 1.
   - The first word gets `"a"`, the second word gets `"aa"`, the third gets `"aaa"`, and so on.

Return the final sentence representing the conversion from `sentence` to Goat Latin.

## Examples

### Example 1
```
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
```

### Example 2
```
Input: sentence = "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
```

## Constraints
- `1 <= sentence.length <= 150`
- `sentence` consists of English letters and spaces.
- `sentence` has no leading or trailing spaces.
- All the words in `sentence` are separated by a single space.

## Approach
1. Define a set of vowels (both lowercase and uppercase) for quick membership checks.
2. Split the sentence into words using `sentence.split()`.
3. For each word with 1-based index `i`:
   - If the first character is a vowel:
     - Keep the word as-is.
   - Otherwise:
     - Move the first character to the end of the word.
   - Append `"ma"` to the transformed word.
   - Append `'a' * i` (i copies of `'a'`) to the end.
   - Collect the transformed word in a result list.
4. Join the transformed words with spaces to form the final Goat Latin sentence.

## Time & Space Complexity
- **Time Complexity:** `O(L)`, where `L` is the length of the sentence, since we process each character a constant number of times.
- **Space Complexity:** `O(L)` for storing the transformed words and the result string.

