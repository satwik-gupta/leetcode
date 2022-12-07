class Solution:
    def validPath(self, n: int, edge: List[List[int]], source: int, destination: int) -> bool:
        e=len(edge)
        adjlist=[[] for i in range(n)]
        for i in range(e):
            adjlist[edge[i][0]].append(edge[i][1])
            adjlist[edge[i][1]].append(edge[i][0])
        stack=[False]*n
        stack[0]=True
        q=[0]
        while(q):
            x=q.pop(0)
            l=adjlist[x]
            for y in l:
                if stack[y]==False:
                    stack[y]=True
                    q.append(y)
        if stack[source]!=True or stack[destination]!=True:
            return False
        return True