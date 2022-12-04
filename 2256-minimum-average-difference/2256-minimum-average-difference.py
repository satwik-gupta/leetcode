class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ps=0
        count=1
        n=len(nums)
        s=sum(nums)
        minav=s
        idx=0
        if(s==0):
            return 0
        for i in range(len(nums)):
            ps+=nums[i]
            s-=nums[i]
            if(i==n-1):
                currentav=abs(ps//(i+1))
            else:
                currentav=abs((ps//(i+1))-(s//(n-i-1)))
            if(currentav<minav):
                idx=i
                minav=min(minav,currentav)
            count+=1
        return idx
    
    