# 23. Merge k Sorted Lists

## Problem Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Examples

### Example 1:
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

### Example 2:
```
Input: lists = []
Output: []
```

### Example 3:
```
Input: lists = [[]]
Output: []
```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order.
- The sum of `lists[i].length` will not exceed `10^4`.

## Approach

Use pairwise merging (divide and conquer):
- Repeatedly merge lists in pairs: `l1` with `l2`, `l3` with `l4`, etc.
- After each pass, the number of lists halves until only one remains.
- Merging two sorted lists is O(n), and we do O(log k) passes.

This results in O(N log k) time complexity, where N is the total number of nodes, and O(1) extra space (not counting recursion if implemented iteratively as below).
