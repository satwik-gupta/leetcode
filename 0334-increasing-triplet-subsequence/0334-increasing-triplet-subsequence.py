class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float("inf")
        for i, n in enumerate(nums):
            if n <=min1:
                min1 = n
            elif n <= min2:
                min2 = n
            else:
                return True
        return False