# Range Sum Query - Immutable

Answer multiple range sum queries in O(1) each using a prefix sum array.

## Approach
- Build a prefix sum array where prefix[i] = sum of nums[0..i-1] (one extra element at start = 0)
- sumRange(left, right) = prefix[right + 1] - prefix[left]

Time Complexity: O(n) build, O(1) query
Space Complexity: O(n)
