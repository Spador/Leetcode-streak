# spador

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2 = set(nums2)
        result = set()
        for n in nums1:
            if n in nums2:
                result.add(n)
        return list(result)
