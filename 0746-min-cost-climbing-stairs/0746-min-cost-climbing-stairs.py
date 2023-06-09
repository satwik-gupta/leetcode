class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
#         def x(cost,n):
            
#             if(n<0):
#                 return 0
#             if(n==1 or n==0):
#                 return cost[n]
#             return cost[n] + min(x(cost,n-1),x(cost,n-2))
#         return min(x(cost,n-1),x(cost,n-2))
        # memo={}
        # memo[0]=cost[0]
        # memo[1]=cost[1]
        # def mincost(cost,n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n]=cost[n]+min(mincost(cost,n-1),mincost(cost,n-2))
        #         return memo[n]
        # return min(mincost(cost,n-1),mincost(cost,n-2))
        if(n==0):
            return cost[0]
        if(n==1):
            return cost[1]
        dp=[0]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])