class Solution:
    def integerBreak(self, n: int) -> int:
        prod=1
        if(n==2):
            return 1
        if(n==3):
            return 2
        if(n==4):
            return 4
        while(n>2):
            n-=3
            prod*=3
        if(n==0):
            return prod
        elif(n==1):
            prod/=3
            prod*=4
            return int(prod)
        else:
            return prod*2
            