# 528. Random Pick with Weight

**Difficulty:** Medium

## Problem Description

You are given a 0-indexed array of positive integers `w` where `w[i]` describes the weight of the ith index.

You need to implement the function `pickIndex()`, which randomly picks an index in the range `[0, w.length - 1]` (inclusive) and returns it. The probability of picking an index `i` is `w[i] / sum(w)`.

For example, if `w = [1, 3]`, the probability of picking index 0 is `1 / (1 + 3) = 0.25` (i.e., 25%), and the probability of picking index 1 is `3 / (1 + 3) = 0.75` (i.e., 75%).

## Examples

### Example 1:
```
Input
["Solution","pickIndex"]
[[[1]],[]]

Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
```

### Example 2:
```
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]

Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
```

## Constraints

- 1 <= w.length <= 10⁴
- 1 <= w[i] <= 10⁵
- pickIndex will be called at most 10⁴ times.

## Approach

This problem can be solved using prefix sums and binary search:

1. **Prefix Sum Array**: Build cumulative sum array where each element represents the sum of weights up to that index
2. **Random Target**: Generate a random number in the range [0, total_sum)
3. **Binary Search**: Use binary search to find the index where the target falls in the prefix sum array
4. **Weighted Selection**: The index found corresponds to the weighted random selection

## Algorithm

1. **Initialization**:
   - Build cumulative sum array from weights
   - Each element cumSum[i] = sum of weights from index 0 to i
2. **pickIndex()**:
   - Generate random target in range [0, total_sum)
   - Use binary search to find the smallest index where cumSum[index] >= target
   - Return the found index

## Implementation Details

- **Cumulative Sum**: Precompute prefix sums for O(1) range queries
- **Binary Search**: Efficiently find target index in O(log n) time
- **Random Generation**: Use uniform distribution for fair selection
- **Index Mapping**: Map random value to weighted index using prefix sums

## Key Optimizations

- **Prefix Sum Precomputation**: Build cumulative array once during initialization
- **Binary Search**: O(log n) lookup time for each pickIndex call
- **Space-Time Tradeoff**: O(n) space for O(log n) query time

## Time Complexity

- **Initialization**: O(n) where n is the length of weights array
  - Build cumulative sum array
- **pickIndex()**: O(log n) for each call
  - Binary search in prefix sum array
- **Space**: O(n) for the cumulative sum array

## Solution

The solution uses prefix sums and binary search:
- Builds cumulative sum array during initialization
- Generates random target and uses binary search to find index
- Returns the weighted random index efficiently
