# 295. Find Median from Data Stream

**Difficulty:** Hard

## Problem Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

## Example

**Input**
```
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
```

**Output**
```
[null, null, null, 1.5, null, 2.0]
```

**Explanation**
```
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

## Constraints

- `-10^5 <= num <= 10^5`
- There will be at least one element in the data structure before calling `findMedian`.
- At most `5 * 10^4` calls will be made to `addNum` and `findMedian`.

## Follow Up

- If all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range `[0, 100]`, how would you optimize your solution?

## Approach

Use two heaps:
- A max-heap `small` to store the smaller half of the numbers (implemented via pushing negative values).
- A min-heap `large` to store the larger half of the numbers.

Maintain the invariants:
- Every element in `small` is less than or equal to every element in `large`.
- The sizes of `small` and `large` differ by at most 1.

Median retrieval:
- If one heap has more elements, the top of that heap is the median.
- If both have the same size, the median is the average of the two tops.

### Complexity
- `addNum`: O(log n)
- `findMedian`: O(1)
- Space: O(n)
