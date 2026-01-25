class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        min_diff=10**5
        nums.sort()
        for i in range(n-k+1):
            min_diff=min(min_diff, nums[i+k-1]-nums[i])
        return min_diff
