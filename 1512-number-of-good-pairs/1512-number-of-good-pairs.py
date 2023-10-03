class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m=max(nums)
        count=[0]*(m+1)
        for i in range(len(nums)):
            count[nums[i]]+=1
        c=0
        for i in count:
            if(i>1):
                c+=(i*(i-1))//2
        return c