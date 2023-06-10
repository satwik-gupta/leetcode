class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)-1
        # if(n==0):
        #     return nums[0]
        # if(n==1):
        #     return max(nums[0],nums[1])
        # def c(nums,n):
        #     if(n==0):
        #         return nums[0]
        #     if(n==1):
        #         return max(nums[1],nums[0])
        #     return max(nums[n]+c(nums,n-2),c(nums,n-1))
        # return max(c(nums,n-1),c(nums,n))
        if(n==0):
            return nums[0]
        if(n==1):
            return max(nums[0],nums[1])
#         memo={}
#         memo[0]=nums[0]
#         memo[1]=max(nums[0],nums[1])
        
#         def c(nums,n):
#             if n in memo:
#                 return memo[n]
#             else:
#                 memo[n]=max(nums[n]+c(nums,n-2),c(nums,n-1))
#                 return memo[n]
#         return max(c(nums,n),c(nums,n-1))
        dp=[0]*(n+1)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n+1):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return max(dp[n],dp[n-1])
    