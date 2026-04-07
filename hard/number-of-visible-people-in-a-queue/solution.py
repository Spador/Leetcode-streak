# spador

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            h = heights[i]
            visible = 0

            while stack and h > stack[-1]:
                visible += 1
                stack.pop()

            if stack:
                visible += 1

            stack.append(h)
            result[i] = visible

        return result
