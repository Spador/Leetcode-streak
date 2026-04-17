# Maximum Distance Between a Pair of Values

Return the maximum j - i where i <= j and nums1[i] <= nums2[j], or 0 if no valid pair exists.

## Approach
- Use two pointers: i starts at 0, j starts at 1
- Advance j each iteration; if nums1[i] > nums2[j] (invalid), advance i instead to try a smaller nums1 value
- The answer is j - i - 1 after the loop (j overshoots by 1 on the last step)

Time Complexity: O(n + m)
Space Complexity: O(1)
