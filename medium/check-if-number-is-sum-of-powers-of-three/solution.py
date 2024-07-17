class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        base3 = [n%3]
        while n != 0:
            n = n//3
            base3.append(n%3)
           
        for x in base3:
            if x == 2:
                return False
        return True 