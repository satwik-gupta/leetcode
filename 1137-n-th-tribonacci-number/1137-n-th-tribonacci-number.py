class Solution:
    def tribonacci(self, n: int) -> int:
        # def c(n):
        #     if(n==0):
        #         return 0
        #     if(n==1):
        #         return 1
        #     if(n==2):
        #         return 1
        #     return c(n-3)+c(n-2)+c(n-1)
        # return c(n)
        memo={}
        memo[0]=0
        memo[1]=1
        memo[2]=1
        def c(n):
            if n in memo:
                return memo[n]
            else:
                memo[n]=c(n-1)+c(n-2)+c(n-3)
                return memo[n]
        return c(n)