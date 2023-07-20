# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums=[]
        mod=10**9 + 7
        def dfs(node):
            if node is None:
                return 0
            sub_sum = dfs(node.left) + dfs(node.right) + node.val
            sums.append(sub_sum)
            return sub_sum
        total= dfs(root)
        res=0
        for i in sums:
            prod=i*(total-i)
            res=max(prod,res)
        return res%mod