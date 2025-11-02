from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # Handle collisions: only when top moves right (positive) and current moves left (negative)
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a  # Sum of sizes (one positive, one negative)
                
                if diff < 0:
                    # Top asteroid explodes, remove it
                    stack.pop()
                elif diff > 0:
                    # Current asteroid explodes, stop processing it
                    a = 0
                else:
                    # Both asteroids explode
                    stack.pop()
                    a = 0
            
            # If current asteroid survives, add it to stack
            if a:
                stack.append(a)
        
        return stack
