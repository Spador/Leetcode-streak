# spador 

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(m*n)
        num1map = {n:i for i, n in enumerate(nums1)}

        result = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in num1map:
                continue
            for j in range(i, len(nums2)):
                if nums2[j] > nums2[i]:
                    result[num1map[nums2[i]]] = nums2[j]
                    break
        return result

        # O(n + m)
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                index = num1map[val]
                result[index] = curr
            if curr in num1map:
                stack.append(curr)
        return result
