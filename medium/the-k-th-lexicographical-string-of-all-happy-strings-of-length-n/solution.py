# spador

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_happy = 3 * (2 ** (n - 1))
        if k > total_happy: return ""
        result = []
        choice = "abc"
        left, right = 1, total_happy

        for i in range(n):
            curr = left
            partition_size = (right - left + 1) // len(choice)

            for ch in choice:
                if curr <= k and k < curr + partition_size:
                    result.append(ch)
                    left = curr
                    right = curr + partition_size - 1
                    choice = "abc".replace(ch, "")
                    break
                curr += partition_size
        return "".join(result)
