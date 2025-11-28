# 494. Target Sum

**Difficulty:** Medium

## Problem Description
You are given an integer array `nums` and an integer `target`.

You want to build an expression out of `nums` by adding one of the symbols `'+'` and `'-'` before each integer in `nums` and then concatenate all the integers.

For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different expressions that you can build, which evaluates to `target`.

## Examples

### Example 1
```
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

### Example 2
```
Input: nums = [1], target = 1
Output: 1
```

## Constraints
- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`
- `0 <= sum(nums[i]) <= 1000`
- `-1000 <= target <= 1000`

## Approach
1. Use backtracking with memoization (caching) to explore all possible ways to assign `+` or `-` to each number.
2. At each index, we have two choices: add `+nums[i]` or add `-nums[i]` to the current total.
3. Use a dictionary to cache results for `(index, total)` pairs to avoid recalculating the same subproblems.
4. Base case: when we've processed all numbers (`index == len(nums)`), return `1` if the total equals the target, otherwise `0`.
5. For each position, recursively explore both options (add or subtract) and sum the results.

## Algorithm
- Initialize a memoization dictionary `dp` with keys `(index, total)`.
- Define recursive function `backtrack(index, total)`:
  - If `index == len(nums)`, return `1` if `total == target`, else `0`.
  - If `(index, total)` is in `dp`, return cached value.
  - Calculate `dp[(index, total)] = backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index])`.
  - Return `dp[(index, total)]`.
- Call `backtrack(0, 0)` to start with index 0 and total 0.

## Time & Space Complexity
- **Time Complexity:** `O(n * m)` where `n` is the number of elements and `m` is the range of possible totals (from minimum total to maximum total).
- **Space Complexity:** `O(n * m)` for the memoization dictionary and recursion stack.
