# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower = -float('inf')
        upper = float('inf')
        res = self.dfs(root,lower,upper)
        return res

    
    def dfs(self,root,lower,upper):
        if not root:
            return True
        if lower>=root.val or root.val>=upper:
            return False
        
        if self.dfs(root.left,lower,root.val)and self.dfs(root.right,root.val,upper):
            return True
        return False

        