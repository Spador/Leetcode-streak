# Top K Frequent Elements

Return the k most frequent elements from an array.

## Approach
- Use bucket sort with frequency counting:
  - Count frequency of each number using hash map
  - Create buckets where index represents frequency
  - Store numbers in their frequency buckets
  - Collect top k elements from highest frequency buckets

Time Complexity: O(n)
Space Complexity: O(n) 