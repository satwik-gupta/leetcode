class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = mn = nums[k]
        low = high = k
        while 0 <= low-1 or high+1 < len(nums): 
            if low == 0 or high+1 < len(nums) and nums[low-1] < nums[high+1]: 
                high += 1
                mn = min(mn, nums[high])
            else: 
                low -= 1
                mn = min(mn, nums[low])
            ans = max(ans, mn * (high-low+1))
        return ans 