# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode],count=0) -> int:
        if root is None:
            return 0
        count ^= 1 << (root.val - 1)
        if root.left is None and root.right is None:
            if count & (count - 1) == 0:
                return 1
            else:
                return 0
        return self.pseudoPalindromicPaths(root.left, count) + self.pseudoPalindromicPaths(root.right, count)