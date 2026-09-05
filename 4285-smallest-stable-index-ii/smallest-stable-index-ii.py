class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        minval=[nums[-1]]
        maxval=-1
        minvalue=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            minvalue=min(minvalue,nums[i])
            minval.append(minvalue)
        for i in range(len(nums)):
            maxval=max(maxval,nums[i])
            if(maxval-minval[len(nums)-1-i]<=k):
                return i
        return -1