# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        graph = collections.defaultdict(list)
        queue = collections.deque([root])

        while queue:
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)
                graph[curr].append(curr.left)
                graph[curr.left].append(curr)
            if curr.right:
                queue.append(curr.right)
                graph[curr].append(curr.right)
                graph[curr.right].append(curr)
        
        queue = collections.deque([(target, 0)])      # tuple to track node and current distance
        visit = set([target])
        result = []
        while queue:
            curr, dist = queue.popleft()
            if dist == k:
                result.append(curr.val)
            else:
                for node in graph[curr]:
                    if node not in visit:
                        queue.append((node, dist + 1))
                        visit.add(node)
        return result
