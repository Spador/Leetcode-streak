# 2013. Detect Squares

**Difficulty:** Medium

## Problem Description
Design a data structure that supports adding points and counting the number of axis-aligned squares that can be formed with a given query point as one corner.

## Example
```
Input: ["DetectSquares","add","add","add","count","count","add","count"]
       [[], [[3,10]], [[11,2]], [[3,2]], [[11,10]], [[14,8]], [[11,2]], [[11,10]]]
Output: [null,null,null,null,1,0,null,2]
```

## Constraints
- `0 <= x, y <= 1000`
- At most 3000 calls to `add` and `count`.

## Approach
1. Store all added points in a list and maintain a frequency map `pointsCount`.
2. For `count(x1, y1)`: iterate all stored points as diagonal candidates `(x2, y2)`. A valid diagonal requires `|x1-x2| == |y1-y2|` and non-zero side length.
3. The other two corners are `(x1, y2)` and `(x2, y1)` — multiply their counts to get combinations.

## Time & Space Complexity
- **add:** `O(1)`
- **count:** `O(n)` where n is total points added
- **Space:** `O(n)`
