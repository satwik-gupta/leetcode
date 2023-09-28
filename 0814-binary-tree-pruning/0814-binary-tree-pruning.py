import gc
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root is None:
                return True
            left,right=dfs(root.left),dfs(root.right)
            if left:
                root.left= None
                gc.collect()
            if right:
                root.right= None
                gc.collect()
            return left and right and root.val==0
        if not dfs(root):
            return root
        else:
            return None