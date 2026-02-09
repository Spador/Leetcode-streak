# 41. First Missing Positive

**Difficulty:** Hard

## Problem Description
Given an unsorted integer array `nums`, return the **smallest positive integer** that is **not present** in `nums`.

You must implement an algorithm that runs in `O(n)` time and uses `O(1)` auxiliary space.

## Examples

### Example 1
```
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
```

### Example 2
```
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
```

### Example 3
```
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
```

## Constraints
- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

## Approach
We use the array itself as a hash: place each positive value `val` in the range `[1, n]` at index `val - 1` by marking that index (e.g. negating the value there). Then the first index `i` where the value is non-negative (or zero) means `i + 1` is the first missing positive.

1. **Normalize negatives:** Replace any negative number with `0` so we can use sign as a marker.
2. **Mark presence:** For each index `i`, let `val = abs(nums[i])`. If `1 <= val <= len(nums)`:
   - If `nums[val - 1] > 0`, set `nums[val - 1] *= -1`.
   - If `nums[val - 1] == 0`, set `nums[val - 1] = -(len(nums) + 1)` (so we don't confuse with "not visited").
3. **Find first missing:** Scan from index `0` to `len(nums) - 1`. The first index `i` where `nums[i] >= 0` means `i + 1` is the first missing positive. If all indices are marked negative, return `len(nums) + 1`.

## Time & Space Complexity
- **Time Complexity:** `O(n)` — a few passes over the array.
- **Space Complexity:** `O(1)` auxiliary (we reuse the input array).
