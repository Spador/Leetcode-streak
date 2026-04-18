# spador

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r = 0, len(colors) - 1
        result = 0
        while l <= r:
            if colors[l] != colors[r]:
                result = r - l
                break
            l += 1
        l, r = 0, len(colors) - 1
        while l <= r:
            if colors[l] != colors[r]:
                result = max(result, r - l)
            r -= 1
        return result
