# Partition Array According to Given Pivot

Rearrange an array so that all elements less than the pivot come first, followed by elements equal to the pivot, then elements greater than the pivot. Maintain the relative order within each group.

## Approach
- Iterate through the array:
  - Add elements less than pivot to the left list
  - Add elements greater than pivot to the right list
  - Count elements equal to pivot
- Concatenate left list, pivots, and right list for the result

Time Complexity: O(n)
Space Complexity: O(n) 