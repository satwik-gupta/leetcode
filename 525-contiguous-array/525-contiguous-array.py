class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
    
        hm={0:-1}
        length=0
        bal = 0
        for i in range(len(nums)):
            if nums[i]==0:
                bal-=1
            else:
                bal+=1
            
            if(bal not in hm):
                hm[bal]=i
            else:
                length=max(length,i-hm[bal])
        return length