# Number of Longest Increasing Subsequence

Return the count of longest strictly increasing subsequences in nums.

## Approach
- Use DP where dp[i] = [length of LIS ending at i, count of such LIS]
- Iterate right to left; for each i scan all j > i where nums[i] < nums[j]
- If extending through j gives a longer LIS, update length and adopt j's count
- If extending through j ties the current best length, add j's count
- Track global max LIS length and accumulate total count across all positions

Time Complexity: O(n²)
Space Complexity: O(n)
