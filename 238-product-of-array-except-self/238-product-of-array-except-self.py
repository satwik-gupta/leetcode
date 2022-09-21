class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        leftRunningProduct = nums[0]
        for i in range(1, N):
            res[i] *= leftRunningProduct
            leftRunningProduct *= nums[i]
            
        rightRunningProduct = nums[-1]
        for i in range(N - 2, -1, -1):
            res[i] *= rightRunningProduct
            rightRunningProduct *= nums[i]
        
        return res