class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n= ans=len(nums)
        arr = sorted(set(nums))
        j = 0
        
        for i in range(len(arr)):
            while j < len(arr) and arr[j] < arr[i] + n:
                j += 1
            
            count = j - i
            ans = min(ans, n - count)

        return ans