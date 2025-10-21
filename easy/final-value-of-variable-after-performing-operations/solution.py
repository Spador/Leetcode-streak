class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ops = {
            "++X": 1,
            "X++": 1,
            "--X": -1,
            "X--": -1
        }
        result = 0
        for x in operations:
            result += ops[x]
        return result
