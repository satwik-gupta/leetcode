class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            currsum=0
            while nums[i]>0:
                currsum+=nums[i]%10
                nums[i]=nums[i]//10
            if currsum==i:
                return i
        return -1