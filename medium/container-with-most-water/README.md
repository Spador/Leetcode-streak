# Container With Most Water

Given an integer array height of length n, find two lines that together with the x-axis form a container containing the most water.

## Approach
- Use two pointers (left and right)
- Calculate area using min height and width
- Move pointer with smaller height inward
- Track maximum area found

Time Complexity: O(n)
Space Complexity: O(1) 