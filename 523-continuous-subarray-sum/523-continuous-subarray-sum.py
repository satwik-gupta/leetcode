class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        if(len(nums)==1):
            return False
        for i in range(1,len(nums)):
            nums[i]=nums[i-1]+nums[i]
        for i in range(len(nums)):
            nums[i]=nums[i]%k
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
        for i in range(len(nums)):
            if i-d[nums[i]]>1:
                return True
        return False