# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        output = []
        self.inorder(root,output)
        l= 0
        r=len(output) - 1
        while l < r:
            sum1 = output[l] + output[r]
            if sum1 == k:
                return True
            else:
                if sum1 < k:
                    l += 1
                else:
                    r -= 1
        return False
        
    def inorder(self,root,output):
        if root == None:
            return
        else:
            self.inorder(root.left,output)
            output.append(root.val)
            self.inorder(root.right,output)