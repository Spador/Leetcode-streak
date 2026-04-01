# Sort Integers by The Number of 1 Bits

Sort an integer array by the number of 1s in each number's binary representation. Break ties by ascending value.

## Approach
- Count set bits for each number using a helper that repeatedly checks the LSB and right-shifts
- Group numbers into a dictionary of min-heaps keyed by bit count
- Iterate over sorted keys and pop from each heap to build the result

Time Complexity: O(n log n)
Space Complexity: O(n)
