# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_list = []
        self.dfs(root)
        return self.sorted_list[k-1]

    def dfs(self,root):
        if not root:
            return
        self.dfs(root.left)
        self.sorted_list.append(root.val)
        self.dfs(root.right)
        