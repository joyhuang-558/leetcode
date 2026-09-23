# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        dfs：返回两个，一个是当前root的高度，一个是当前root 最大dia
        '''
        def dfs(root):
            if not root:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)

            height = max(left[0],right[0])+1
            dia = max(left[0]+right[0],left[1],right[1])
            return [height,dia]
        
        
        return dfs(root)[1]