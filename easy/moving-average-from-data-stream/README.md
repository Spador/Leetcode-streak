# 346. Moving Average from Data Stream

**Difficulty:** Easy

## Problem Description
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:

- `MovingAverage(int size)` initializes the object with the size of the window `size`.
- `double next(int val)` returns the moving average of the last `size` values of the stream.

## Example
```
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]

Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1);  // return 1.0   = 1 / 1
movingAverage.next(10); // return 5.5   = (1 + 10) / 2
movingAverage.next(3);  // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5);  // return 6.0   = (10 + 3 + 5) / 3
```

## Constraints
- `1 <= size <= 1000`
- `-10^5 <= val <= 10^5`
- At most `10^4` calls will be made to `next`.

## Approach
We maintain a fixed-size sliding window using a queue and a running sum:

1. Store the window size `size` and a queue (e.g. `deque`) to hold the last at-most-`size` values.
2. Keep a running sum `movingSum` of the values in the queue.
3. For each call to `next(val)`:
   - Push `val` to the queue and add it to `movingSum`.
   - If the queue length exceeds `size`, remove the oldest value from the queue and subtract it from `movingSum`.
   - The current moving average is `movingSum / len(queue)`.

This ensures `O(1)` amortized time per `next` call.

## Time & Space Complexity
- **Time Complexity:** `O(1)` per `next` call (amortized).
- **Space Complexity:** `O(size)` for the queue and constant extra space for the running sum.
