class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        l=0
        prod=1
        count=0
        for r in range(len(nums)):
            if(nums[r]*prod)<k:
                count+=1 + (r-l)
                prod*=nums[r]
            else:
                while(nums[r]*prod)>=k and l<=r:
                    prod/=nums[l]
                    l+=1
                count+=1 + (r-l)
                prod*=nums[r]
        return count

