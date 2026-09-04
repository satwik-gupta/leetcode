class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxval=[nums[0]]
        minval=[nums[-1]]
        maxvalue=nums[0]
        minvalue=nums[-1]
        for i in range(1,len(nums)):
            maxvalue=max(maxvalue,nums[i])
            maxval.append(maxvalue)
        for i in range(len(nums)-2,-1,-1):
            minvalue=min(minvalue,nums[i])
            minval.append(minvalue)
        for i in range(len(nums)):
            if(maxval[i]-minval[len(nums)-1-i]<=k):
                return i
        return -1