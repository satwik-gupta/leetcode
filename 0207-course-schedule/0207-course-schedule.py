class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(n)]
        indeg=[0]*n
        for i,j in prerequisites:
            adj[j].append(i)
            indeg[i]+=1
        q=[]
        c=0
        for deg in range(n):
            if(indeg[deg]==0):
                q.append(deg)
                c+=1
        while(q):
            x=q.pop()
            y=adj[x]
            for s in y:
                indeg[s]-=1
                if(indeg[s]==0):
                    q.append(s)
                    c+=1
        if(c==n):
            return True
        else:
            return False