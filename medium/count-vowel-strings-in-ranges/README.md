# Count Vowel Strings in Ranges

Count the number of strings in given ranges that start and end with a vowel.

## Approach
- Use prefix sum to efficiently answer range queries
- For each word, check if it starts and ends with a vowel
- Build prefix sum array of valid words
- For each query, subtract prefix sums to get count in range

Time Complexity: O(n + q) where n is number of words and q is number of queries
Space Complexity: O(n) 