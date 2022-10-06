class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if(n>2**31-1):
            return -1
        w=str(n)
        w=list(w)
        temp=None
        for i in range(len(w)-1,0,-1):
            if(w[i]>w[i-1]):
                temp=w[i-1]
                idx=i-1
                break
        if(not temp):
            return -1
        for i in range(len(w)-1,-1,-1):
            if(w[i]>temp):
                w[i],w[idx]=w[idx],w[i]
                break
        res=int("".join(w[:idx+1]+sorted(w[idx+1:])))
        if(res>2**31-1):
            return -1
        return res