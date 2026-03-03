# spador

# Reverse entire list.
# Reverse first k element in list
# Reverse rest of the elements in the list

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def rotate(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        rotate(0, n - 1)
        rotate(0, k - 1)
        rotate(k, n -1)
