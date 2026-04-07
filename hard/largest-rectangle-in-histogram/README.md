# Largest Rectangle in Histogram

Return the area of the largest rectangle that can be formed in a histogram.

## Approach
- Use a monotonic increasing stack storing (start_index, height) pairs
- When a shorter bar is encountered, pop all taller bars from the stack and compute their max area extending back to their start index
- The start index of the current bar is updated to the leftmost popped index (it can extend that far left)
- After the loop, compute area for all remaining bars in the stack extending to the end

Time Complexity: O(n)
Space Complexity: O(n)
