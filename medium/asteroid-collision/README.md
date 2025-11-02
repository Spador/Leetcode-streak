# 735. Asteroid Collision

**Difficulty:** Medium

## Problem Description

We are given an array `asteroids` of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Examples

### Example 1:
```
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
```

### Example 2:
```
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```

### Example 3:
```
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
```

### Example 4:
```
Input: asteroids = [3,5,-6,2,-1,4]
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.
```

## Constraints

- 2 <= asteroids.length <= 10⁴
- -1000 <= asteroids[i] <= 1000
- asteroids[i] != 0

## Approach

This problem can be solved using a stack:

1. **Stack Processing**: Use stack to track asteroids moving right
2. **Collision Detection**: When asteroid moves left (negative), check collision with top of stack
3. **Collision Resolution**: Compare sizes and handle explosions
4. **Result Building**: Stack contains remaining asteroids

## Algorithm

1. Initialize empty stack
2. For each asteroid:
   - While stack is not empty and top moves right and current moves left:
     - Calculate collision: diff = stack[-1] + current
     - If diff < 0: top explodes, pop from stack
     - If diff > 0: current explodes, set current to 0
     - If diff == 0: both explode, pop from stack and set current to 0
   - If current asteroid survives (not 0), push to stack
3. Return stack as result

## Implementation Details

- **Stack-based**: Use stack to handle collisions
- **Direction Check**: Only collide when right-moving meets left-moving
- **Size Comparison**: Compare absolute values to determine winner
- **Collision Loop**: Continue checking until no more collisions

## Key Optimizations

- **O(n) Time**: Each asteroid processed once
- **Stack Efficiency**: Efficient collision handling
- **Single Pass**: Process asteroids in order

## Time Complexity

- **Time**: O(n) where n is the number of asteroids
  - Each asteroid is pushed and popped at most once
- **Space**: O(n) for the stack in worst case

## Solution

The solution uses a stack-based approach:
- Processes asteroids in order
- Handles collisions between right-moving and left-moving asteroids
- Returns the final state after all collisions
