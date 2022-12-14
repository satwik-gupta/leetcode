class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for i in range(n)]
        indeg=[0]*n
        for i,j in prerequisites:
            adj[j].append(i)
            indeg[i]+=1
        q=[]
        c=0
        res=[]
        for deg in range(n):
            if(indeg[deg]==0):
                q.append(deg)
                c+=1
        while(q):
            x=q.pop()
            y=adj[x]
            res.append(x)
            for s in y:
                indeg[s]-=1
                if(indeg[s]==0):
                    q.append(s)
                    c+=1
        if(c==n):
            return res
        else:
            return []