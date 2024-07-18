from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        count = 0

        for n in nums:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                count += 1
        
        for i in range(count):
            left.append(pivot)
        for i in range(len(right)):
            left.append(right[i])
        return left 