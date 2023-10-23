import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start=bisect.bisect_left(nums,target)      
        end=bisect.bisect_right(nums,target)
        if start>end-1:
            return [-1,-1]
        return [start,end-1]