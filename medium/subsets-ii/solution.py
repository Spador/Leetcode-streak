# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(index, subset):
            if index == len(nums):
                result.append(subset[:])
                return
            
            # Include the current element
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

            # Skip all duplicates of the current element
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            backtrack(index + 1, subset)
        
        backtrack(0, [])
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 2]
    result1 = solution.subsetsWithDup(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2
    nums2 = [0]
    result2 = solution.subsetsWithDup(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
