

from typing import Optional
class Solution:
    def helper(self,node,visited):
        if node is None:
            return None
        newnode=Node(node.val)
        visited[node.val]=newnode
        for adjnode in node.neighbors:
            if adjnode.val not in visited:
                newnode.neighbors.append(self.helper(adjnode,visited))
            else:
                newnode.neighbors.append(visited[adjnode.val])
        return newnode
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.helper(node,{})