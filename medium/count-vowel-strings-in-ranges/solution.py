from typing import List
from itertools import accumulate

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        return (p := [0, *accumulate(word[0] in 'aeiou' and word[-1] in 'aeiou' for word in words)]) and [p[r+1]-p[l] for l, r in queries] 