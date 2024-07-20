class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longestSeq = max(length, longestSeq)
                if longestSeq > len(nums)//2:
                    return longestSeq
        return longestSeq
