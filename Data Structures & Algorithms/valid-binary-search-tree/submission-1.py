# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lo = float('-inf')
        hi = float('inf')
        return self.dfs(root,lo,hi)
    def dfs(self,root,lo,hi):
        if root is None:
            return True
        if root.val>=hi or root.val<=lo:
            return False
        return self.dfs(root.left,lo,root.val) and self.dfs(root.right,root.val,hi)
       


        