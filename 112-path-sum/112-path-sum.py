# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,ans,path,targetSum):
        if(root==None):
            return
        path.append(root.val)
        if(root.left==None and root.right==None and root.val==targetSum):
            ans.append(list(path))
        self.dfs(root.left,ans,path,targetSum-root.val)
        self.dfs(root.right,ans,path,targetSum-root.val)
        path.pop()
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans=[]
        self.dfs(root,ans,path,targetSum)
        if(len(ans)>0):
            return True
        else:
            return False