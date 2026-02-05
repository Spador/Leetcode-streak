# spador

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waits = [0] * len(temperatures)
        stack = []      # [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, day = stack.pop()
                waits[day] = i - day
            stack.append([temp, i])
        return waits
        
