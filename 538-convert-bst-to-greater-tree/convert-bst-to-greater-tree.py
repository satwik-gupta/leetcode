# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total=0
        def dfs(node):
            if not node:
                return
            nonlocal total
            dfs(node.right)
            temp=node.val
            node.val+=total
            total+=temp
            dfs(node.left)
        dfs(root)
        return root