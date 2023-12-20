class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        count=0
        ans[0]=0
        for i in range(1,n+1):
            if(i&1):
                ans[i]=ans[(i-1)//2] +1
            else:
                ans[i]=ans[i//2]
        return ans