# 359. Logger Rate Limiter

**Difficulty:** Easy

## Problem Description

Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

- `Logger()` Initializes the logger object.
- `bool shouldPrintMessage(int timestamp, string message)` Returns true if the message should be printed in the given timestamp, otherwise returns false.

## Examples

### Example 1:
```
Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]

Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
```

## Constraints

- 0 <= timestamp <= 10⁹
- Every timestamp will be passed in non-decreasing order (chronological order).
- 1 <= message.length <= 30
- At most 10⁴ calls will be made to shouldPrintMessage.

## Approach

This problem can be solved using a hashmap to track the last printed timestamp for each message:

1. **HashMap Storage**: Store message -> last printed timestamp mapping
2. **Time Check**: Check if current timestamp is at least 10 seconds after last print
3. **Update**: Update the timestamp if message should be printed

## Algorithm

1. Initialize a dictionary to store message -> last timestamp
2. For `shouldPrintMessage(timestamp, message)`:
   - If message not in dictionary, add it with current timestamp and return true
   - If message exists and timestamp >= last_timestamp + 10, update timestamp and return true
   - Otherwise, return false

## Implementation Details

- **Dictionary Lookup**: O(1) lookup for message timestamps
- **Time Comparison**: Check if enough time has passed
- **State Update**: Update timestamp when message is printed

## Key Optimizations

- **O(1) Lookup**: HashMap provides constant time access
- **Simple Logic**: Straightforward time-based rate limiting
- **Memory Efficient**: Only stores messages that have been printed

## Time Complexity

- **Time**: O(1) for each `shouldPrintMessage` call
  - Dictionary lookup and update are O(1)
- **Space**: O(m) where m is the number of unique messages

## Solution

The solution uses a hashmap to track last printed timestamp:
- Stores message -> timestamp mapping
- Checks if 10 seconds have passed since last print
- Returns true if message should be printed, false otherwise
