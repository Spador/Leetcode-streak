##spador
class Solution:
    def maxDifference(self, s: str) -> int:
        store = {}
        for c in s:
            store[c] = 1 + store.get(c,0)
        
        maxOdd = 0
        minEven = 100

        for n in store.values():
            if n % 2 == 1:
                if n > maxOdd:
                    maxOdd = n
            else:
                if n < minEven:
                    minEven = n
        
        return (maxOdd - minEven)
