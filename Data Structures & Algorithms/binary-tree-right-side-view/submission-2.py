# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.bfs(root)
        return self.res
    def bfs(self,root):
        q = deque([root])
        if root is None:
            return []
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if i == size-1:
                    self.res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)






        