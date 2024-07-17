from itertools import accumulate

class Solution:
    def maxScore(self, s: str) -> int:
        prefix_zeros = list(accumulate(1 if char == '0' else 0 for char in s))

        max_score = 0
        for i in range(1, len(s)):
            count_zeros_left = prefix_zeros[i-1]
            count_one_right = (len(s) - i) - (prefix_zeros[-1] - prefix_zeros[i-1])
            max_score = max(max_score, count_zeros_left + count_one_right)
        
        return max_score 