class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            prefix.append(sum)
        maxsum=prefix[-1]
            
        res=[]
        revsum=0
        
        for i in range(0,len(nums)):
            if(i==0):
                val=(prefix[-1]-prefix[0])-(nums[i]*(len(nums)-1-i))
            elif(i==len(nums)-1):
                val=(nums[i]*i -(prefix[i-1]))
            else:
                val=(nums[i]*i -(prefix[i-1]))+((maxsum-prefix[i])-(nums[i]*(len(nums)-i-1)))
            res.append(val)
        return res