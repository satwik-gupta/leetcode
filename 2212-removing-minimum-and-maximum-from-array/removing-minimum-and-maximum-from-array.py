class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini=10**5
        maxi=-10**5
        a,b=0,0
        n=len(nums)
        for i in range(len(nums)):
            if(nums[i]>maxi):
                maxi=nums[i]
                a=i
            if(nums[i]<mini):
                mini=nums[i]
                b=i
        print(a,b)

        return min(n-abs(a-b),max(a,b),max(n-a,n-b)-1)+1
