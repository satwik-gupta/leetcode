class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        minprod=nums[0]*nums[1]
        maxprod=nums[-1]*nums[-2]
        return (maxprod-minprod)