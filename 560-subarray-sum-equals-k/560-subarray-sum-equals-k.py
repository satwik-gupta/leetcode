class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefixSum approach used
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        
        ans=0
        prefsum={0:1}
        for i in nums:
            extra=i-k
            if(extra in prefsum):
                ans+=prefsum[extra]
            if(i not in prefsum):
                prefsum[i]=1
            else:
                prefsum[i]+=1
        return ans