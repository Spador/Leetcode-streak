class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = []
        for i, num in enumerate(nums):
            if num:
                self.nums.append((i, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i, j = 0, 0
        v1 = self.nums
        v2 = vec.nums
        result = 0
        while i < len(v1) and j < len(v2):
            if v1[i][0] < v2[j][0]:
                i += 1
            elif v1[i][0] > v2[j][0]:
                j += 1
            else:
                result += v1[i][1] * v2[j][1]
                i += 1
                j += 1
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
