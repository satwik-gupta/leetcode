class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=1
        k=1
        while(r<len(nums)):
            if(nums[l]!=nums[r]):
                l+=1
                nums[l]=nums[r]
                k+=1
            r+=1   
        return k