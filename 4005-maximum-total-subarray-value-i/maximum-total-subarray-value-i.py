class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1=max(nums)
        m2=min(nums)
        return (m1-m2)*k