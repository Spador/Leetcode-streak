# spador

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        revflag = False
        queue = collections.deque([root] if root else [])
        result = []
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                if not revflag:
                    level.append(node.val)
                else:
                    level = [node.val] + level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            revflag = not revflag
            result.append(level)
        return result
