# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        return self.dfs(root,float('-inf'))

    def dfs(self,root,max_v):
        if root is None:
            return
        if root.val >= max_v:
            self.count += 1
            max_v = root.val
        self.dfs(root.left,max_v)
        self.dfs(root.right,max_v)
        return self.count
            
            

    
        