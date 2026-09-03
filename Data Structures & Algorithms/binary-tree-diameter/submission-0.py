# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dep(root)
        return self.res



    def dep(self,root):
        if root is None:
            return 0
        left_d = self.dep(root.left)
        right_d = self.dep(root.right)
        self.dia = left_d+right_d
        self.res = max(self.res,self.dia)
        return 1+max(left_d,right_d)

        