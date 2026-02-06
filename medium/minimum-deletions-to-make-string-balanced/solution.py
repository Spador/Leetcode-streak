# spador

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count_right = 0
        for ch in s:
            a_count_right += 1 if ch == "a" else 0
        
        b_count_left = 0
        result = len(s)
        for i, ch in enumerate(s):
            if ch == 'a':
                a_count_right -= 1
            result = min(result, b_count_left + a_count_right)
            if ch == 'b':
                b_count_left += 1
        return result
