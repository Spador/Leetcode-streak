# 1570. Dot Product of Two Sparse Vectors

**Difficulty:** Medium

## Problem Description
Given two sparse vectors, compute their dot product.

Implement class `SparseVector`:

- `SparseVector(nums)` initializes the object with the vector `nums`.
- `dotProduct(vec)` computes the dot product between the instance of `SparseVector` and `vec`.

A sparse vector is a vector that has mostly zero values; you should store the sparse vector efficiently and compute the dot product between two `SparseVector` objects.

## Examples

### Example 1
```
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1), v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
```

### Example 2
```
Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
```

### Example 3
```
Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
```

## Constraints
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] <= 100`

## Approach
We store each sparse vector efficiently by keeping only the **non-zero entries** as a list of `(index, value)` pairs. Then we compute the dot product using a two-pointer merge-like traversal.

### Storage
- In the constructor, iterate over `nums`.
- For each index `i` where `nums[i] != 0`, store a pair `(i, nums[i])` in an internal list `self.nums`.

### Dot Product
Given two `SparseVector` instances `v1` and `v2`:
- Let `v1.nums` and `v2.nums` be the lists of non-zero `(index, value)` pairs, sorted by index.
- Use two pointers `i` and `j` starting at `0`.
- While both pointers are within bounds:
  - If `v1.nums[i].index < v2.nums[j].index`, increment `i`.
  - Else if `v1.nums[i].index > v2.nums[j].index`, increment `j`.
  - Else (indices equal), multiply the values and add to the result, then increment both `i` and `j`.

This is similar to merging two sorted lists and only multiplying when indices match.

## Time & Space Complexity
- **Time Complexity:**
  - Construction: `O(k)` where `k` is the length of `nums`.
  - Dot Product: `O(k1 + k2)` where `k1` and `k2` are the number of non-zero entries in the two vectors.
- **Space Complexity:** `O(k)` per vector for storing non-zero entries.
