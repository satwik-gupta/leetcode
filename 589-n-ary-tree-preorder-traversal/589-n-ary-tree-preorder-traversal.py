"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def prepre(root):
            if root:
                for i in root.children:
                    s.append(i.val)
                    prepre(i)
        
        
        if root is None:
            return []
        s=[]
        if root:
            s.append(root.val)
        prepre(root)
        return s
            
            