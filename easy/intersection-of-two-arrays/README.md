# Intersection of Two Arrays

Return an array of unique elements present in both nums1 and nums2.

## Approach
- Convert nums2 to a set for O(1) lookups
- Iterate through nums1 and add elements found in nums2 to a result set (handles duplicates automatically)
- Return the result set as a list

Time Complexity: O(n + m)
Space Complexity: O(n + m)
