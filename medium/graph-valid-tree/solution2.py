# spador

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {node: [] for node in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(n, prev):
            if n in visit:
                return False

            visit.add(n)
            for nei in adj[n]:
                if nei != prev:
                    if not dfs(nei, n):
                        return False
            return True

        return dfs(0, -1) and n == len(visit)
