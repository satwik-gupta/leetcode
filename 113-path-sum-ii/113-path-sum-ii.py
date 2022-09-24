# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,path,ans,targetSum):
        if root is None:
            return
        path.append(root.val)
        if not root.left and not root.right and root.val==targetSum:
            ans.append(list(path))
        self.dfs(root.left,path,ans,targetSum-root.val)
        self.dfs(root.right,path,ans,targetSum-root.val)
        path.pop()
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        self.dfs(root,[],ans,targetSum)
        return ans