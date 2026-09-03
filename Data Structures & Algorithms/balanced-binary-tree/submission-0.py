# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dep(root) != -1
        
    

    def dep(self,root):
        if root is None:
            return 0
        left_d = self.dep(root.left)
        if left_d == -1:
            return -1
        right_d = self.dep(root.right)
        if right_d == -1:
            return -1
        if abs(left_d - right_d)>1:
            return -1
        return 1+max(left_d,right_d)
        



        