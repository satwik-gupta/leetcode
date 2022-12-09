# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root,mini,maxi,res):
            if not root:
                return
            res[0]=max(res[0],abs(mini-root.val),abs(maxi-root.val))
            mini = min(root.val, mini)
            maxi = max(root.val, maxi)
            dfs(root.left,mini,maxi,res)
            dfs(root.right,mini,maxi,res)
        res=[0]
        dfs(root, root.val, root.val, res)
        return res[0]