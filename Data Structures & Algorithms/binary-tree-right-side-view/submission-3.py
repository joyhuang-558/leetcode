# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if cur:
                    if i == size-1:
                        res.append(cur)
                    q.append(cur.left)
                    q.append(cur.right)
        return res

        