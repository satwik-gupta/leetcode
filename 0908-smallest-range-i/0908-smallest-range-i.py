class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        s= (nums[-1]-k)-(nums[0]+k)
        if(s<0):
            return 0
        else:
            return s