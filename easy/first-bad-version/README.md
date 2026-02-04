# 278. First Bad Version

**Difficulty:** Easy

## Problem Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the **first bad** one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## Examples

### Example 1
```
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
```

### Example 2
```
Input: n = 1, bad = 1
Output: 1
```

## Constraints
- `1 <= bad <= n <= 2^31 - 1`

## Approach
We use **binary search** to minimize the number of calls to `isBadVersion`.

1. Maintain two pointers `first = 1` and `last = n`.
2. While `first < last`:
   - Compute `mid = first + (last - first) // 2` to avoid overflow.
   - If `isBadVersion(mid)` is `false`, it means the first bad version must be **after** `mid`, so set `first = mid + 1`.
   - Otherwise, the first bad version is at or **before** `mid`, so set `last = mid`.
3. When the loop ends, `first` (which equals `last`) will be the index of the first bad version.

## Time & Space Complexity
- **Time Complexity:** `O(log n)` — each call to `isBadVersion` halves the search range.
- **Space Complexity:** `O(1)` extra space.
