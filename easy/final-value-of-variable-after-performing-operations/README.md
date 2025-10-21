# 2011. Final Value of Variable After Performing Operations

**Difficulty:** Easy

## Problem Description

There is a programming language with only four operations and one variable X:

- ++X and X++ increments the value of the variable X by 1.
- --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

## Examples

### Example 1:
```
Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
```

### Example 2:
```
Input: operations = ["++X","++X","X++"]
Output: 3
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
```

### Example 3:
```
Input: operations = ["X++","++X","--X","X--"]
Output: 0
Explanation: The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.
```

## Constraints

- 1 <= operations.length <= 100
- operations[i] will be either "++X", "X++", "--X", or "X--".

## Approach

This problem can be solved by mapping each operation to its corresponding value change:

1. **Operation Mapping**: Create a mapping from operation strings to their values (+1 or -1).
2. **Accumulation**: Sum all the values to get the final result.
3. **Simple Iteration**: Process each operation and accumulate the result.

## Algorithm

1. Create a dictionary mapping each operation to its value:
   - "++X" and "X++" → +1
   - "--X" and "X--" → -1
2. Initialize result to 0
3. Iterate through each operation and add its mapped value
4. Return the final accumulated result

## Implementation Details

- **Dictionary Mapping**: Use a hash map for O(1) operation lookup
- **Simple Accumulation**: Add each operation's value to running total
- **No Edge Cases**: All operations are guaranteed to be valid

## Key Optimizations

- **Hash Map Lookup**: O(1) time complexity for each operation
- **Single Pass**: Process all operations in one iteration
- **Minimal Space**: Only store the mapping and result

## Time Complexity

- **Time**: O(n) where n is the number of operations
  - We process each operation exactly once
- **Space**: O(1) for the mapping dictionary (constant size)

## Solution

The solution uses a dictionary mapping approach:
- Maps each operation string to its corresponding value change
- Accumulates all values to get the final result
- Handles all four possible operations efficiently
- Returns the final value after all operations
