# 40. Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, comb, rem):
            # Base case: found a valid combination
            if rem == 0:
                result.append(comb[:])
                return
            # Early termination: remaining target is negative
            if rem <= 0:
                return
            
            prev = -1  # Track previous element to avoid duplicates
            
            for i in range(index, len(candidates)):
                # Skip duplicates at the same level
                if candidates[i] == prev:
                    continue 
                
                # Add current candidate to combination
                comb.append(candidates[i])
                # Recursively search with updated target and next index
                backtrack(i + 1, comb, rem - candidates[i])
                # Backtrack: remove the candidate
                comb.pop()
                # Update previous for duplicate checking
                prev = candidates[i]   
        
        backtrack(0, [], target)
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    result1 = solution.combinationSum2(candidates1, target1)
    print(f"Input: candidates = {candidates1}, target = {target1}")
    print(f"Output: {result1}")
    print()
    
    # Test case 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    result2 = solution.combinationSum2(candidates2, target2)
    print(f"Input: candidates = {candidates2}, target = {target2}")
    print(f"Output: {result2}")
