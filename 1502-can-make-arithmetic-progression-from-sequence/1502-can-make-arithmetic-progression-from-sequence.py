class Solution:
    def canMakeArithmeticProgression(self, nums: List[int]) -> bool:
        nums.sort()
        d=nums[1]-nums[0]
        
        for i in range(2,len(nums)):
            if(nums[i]-nums[i-1]==d):
                continue
            else:
                return False
        return True