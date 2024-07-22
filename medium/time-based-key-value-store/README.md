# 981. Time Based Key-Value Store

## Problem Description

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

- `TimeMap()` Initializes the object of the data structure.
- `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
- `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

## Examples

### Example 1:
```
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
```

## Constraints

- `1 <= key.length, value.length <= 100`
- `key` and `value` consist of lowercase English letters and digits.
- `1 <= timestamp <= 10^7`
- All the timestamps `timestamp` of `set` are strictly increasing.
- At most `2 * 10^5` calls will be made to `set` and `get`.

## Approach

The solution uses a **hash map with binary search**:

1. **Data Structure**: Use a hash map where keys map to lists of `[value, timestamp]` pairs
2. **Set Operation**: Append new `[value, timestamp]` pairs to the list for the given key
3. **Get Operation**: Use binary search to find the largest timestamp ≤ the requested timestamp
   - Since timestamps are strictly increasing, the list is already sorted
   - Binary search for the target timestamp or the largest timestamp less than it
   - Return the corresponding value, or `""` if no valid timestamp found

**Key Insight**: Since timestamps are strictly increasing, we can use binary search for efficient retrieval.

## Time Complexity

- **Set**: O(1) - Simple append operation
- **Get**: O(log n) - Binary search on the timestamp list for the key

## Space Complexity

O(n) where n is the total number of set operations - storing all key-value-timestamp combinations.
