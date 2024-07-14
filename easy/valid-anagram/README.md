# Valid Anagram

Check if two strings are anagrams of each other.

## Approach
- Use hash map to track character frequencies
- First check if strings have same length
- Count characters in first string
- Decrement counts for second string
- Remove characters when count reaches zero
- Return false if character not found or count becomes negative

Time Complexity: O(n)
Space Complexity: O(k) where k is the number of unique characters 