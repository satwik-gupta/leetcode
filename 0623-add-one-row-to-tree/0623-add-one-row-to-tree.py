# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            root = TreeNode(val, root, None)
        q = [(root, 1)]
        
        while q:
            cur, d = q.pop(0)
            if d == depth - 1:
                tmpL = cur.left
                tmpR = cur.right
                cur.right = TreeNode(val,None,tmpR)
                cur.left = TreeNode(val,tmpL,None)
            else:
                if cur.left:
                    q.append((cur.left, d+1))
                if cur.right:
                    q.append((cur.right,d+1))
        return root