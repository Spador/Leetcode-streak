# 846. Hand of Straights

**Difficulty:** Medium

## Problem Description
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `i`th card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

## Examples

### Example 1
```
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
```

### Example 2
```
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
```

## Constraints
- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`
- `1 <= groupSize <= hand.length`

> Note: This question is the same as 1296: Divide Array in Sets of K Consecutive Numbers.

## Approach
We need to check whether the multiset of card values in `hand` can be partitioned into groups of size `groupSize` where each group consists of consecutive integers.

Key ideas:
1. **Length check**: If `len(hand) % groupSize != 0`, it's impossible to divide all cards into groups of equal size, so return `False`.
2. Use a **frequency map** (`cardmap`) to count how many times each card value appears.
3. Use a **min-heap** of the distinct card values so we can always start forming groups from the **smallest** available card.
4. Repeatedly:
   - Let `start` be the smallest card value currently in the heap.
   - Try to build a group `[start, start + 1, ..., start + groupSize - 1]`.
   - For each value `i` in this range:
     - If `i` is not in `cardmap`, we cannot form a consecutive group, so return `False`.
     - Decrement `cardmap[i]`. 
     - If `cardmap[i]` becomes `0`, then this card value is exhausted and must match the current smallest in the heap; otherwise the ordering is broken and we return `False`.
     - When `cardmap[i]` hits `0` and `i` is the heap's minimum, pop it from the heap.
5. If we manage to consume all cards according to these rules, return `True`.

This ensures we always form groups from the smallest remaining value and enforce consecutiveness and correct counts.

## Time & Space Complexity
- **Time Complexity:** `O(n log n)` where `n = len(hand)`:
  - Building the heap from distinct values is `O(m)` where `m <= n`.
  - Each card is processed once, and heap operations are `O(log m)` in the worst case.
- **Space Complexity:** `O(m)` for the frequency map and heap, where `m` is the number of distinct card values.

