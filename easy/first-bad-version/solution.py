# spador

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first, last = 1, n
        while first < last:
            mid = first + ((last - first) // 2)
            if not isBadVersion(mid):
                first = mid + 1
            else:
                last = mid

        return first
