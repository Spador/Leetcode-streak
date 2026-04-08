# The k-th Lexicographical String of All Happy Strings of Length n

Return the k-th happy string of length n in lexicographical order, or "" if fewer than k exist.

## Approach
- Total happy strings = 3 * 2^(n-1); return "" immediately if k exceeds this
- Use binary search-style partitioning: at each position divide the remaining range equally among available characters (2 or 3 choices)
- For each position find which partition k falls into, append that character, narrow the range, and remove that character from future choices to avoid consecutive duplicates

Time Complexity: O(n)
Space Complexity: O(n)
