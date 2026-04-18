# Two Furthest Houses With Different Colors

Return the maximum distance between two houses with different colors.

## Approach
- The optimal pair must include either the first or last house
- First pass: fix right end (last index), advance left pointer until colors differ — captures the best pair anchored at the right
- Second pass: fix left end (index 0), retreat right pointer until colors differ — captures the best pair anchored at the left
- Return the maximum of both results

Time Complexity: O(n)
Space Complexity: O(1)
