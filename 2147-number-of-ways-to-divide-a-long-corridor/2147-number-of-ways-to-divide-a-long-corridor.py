class Solution:
    def numberOfWays(self, c: str) -> int:
        idx=[]
        cs=0
        mod=10**9 +7
        for i in range(len(c)):
            if(c[i]=='S'):
                cs+=1
                idx.append(i)
        if(cs%2!=0 or cs==0):
            return 0
        res=1
        prev=idx[1]
        for i in range(2,len(idx),2):
            l=idx[i]-prev
            res=(res*l)%mod
            prev=idx[i+1]
        return res