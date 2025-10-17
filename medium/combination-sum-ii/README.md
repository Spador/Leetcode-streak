# 40. Combination Sum II

**Difficulty:** Medium

## Problem Description

Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:** The solution set must not contain duplicate combinations.

## Examples

### Example 1:
```
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```

### Example 2:
```
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
```

## Constraints

- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`
- `1 <= target <= 30`

## Approach

This problem is similar to Combination Sum, but with two key differences:
1. Each number can only be used **once** (not multiple times)
2. The array may contain **duplicates**, and we must avoid duplicate combinations

### Algorithm:
1. **Sort the array** to group duplicates together
2. **Use backtracking** to explore all possible combinations
3. **Skip duplicates** by tracking the previous element and avoiding repeated use
4. **Early termination** when remaining target becomes negative
5. **Base case** when remaining target equals 0

### Key Insights:
- Sort the array first to handle duplicates efficiently
- Use a loop instead of recursive calls to avoid duplicate combinations
- Track the previous element to skip duplicates in the same level
- Each element can only be used once, so increment index after selection

### Time Complexity
- **Time:** O(2^n) where n is the length of the array (worst case)
- **Space:** O(target) for the recursion stack

### Space Complexity
- **Space:** O(2^n) for storing all combinations

## Solution Strategy

The solution uses backtracking with duplicate handling:

1. Sort the input array to group duplicates
2. Use a for loop to iterate through candidates starting from current index
3. Skip duplicate elements by checking if current element equals previous element
4. For each valid element:
   - Add it to current combination
   - Recursively search with updated target and next index
   - Remove element (backtrack)
   - Update previous element for duplicate checking

This approach ensures no duplicate combinations while exploring all valid paths.
