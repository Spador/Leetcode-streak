from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index: int, subset: List[int], total: int) -> None:
            if total == target:
                result.append(subset.copy())
                return
            
            if total > target or index >= len(candidates):
                return
            
            # decision to include candidates[index]
            subset.append(candidates[index])
            backtrack(index, subset, total + candidates[index])

            # decision to NOT include candidates[index]
            subset.pop()
            backtrack(index + 1, subset, total)
        
        backtrack(0, [], 0)
        return result
