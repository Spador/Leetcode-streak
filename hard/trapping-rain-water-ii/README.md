# Trapping Rain Water II

Return the total volume of water trapped in a 2D elevation map after raining.

## Approach
- Push all border cells into a min-heap and mark them visited (set to -1)
- Process the heap: for each cell popped, track the running max height seen so far
- Water trapped at this cell = max height so far - cell height (the current cell acts as a "bucket" bounded by the tallest border seen)
- Push unvisited neighbors into the heap and mark them visited

Time Complexity: O(m * n * log(m * n))
Space Complexity: O(m * n)
