# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        l=1
        r=n-2
        while(l!=r):
            mid=(l+r)//2
            if(mountain_arr.get(mid)<mountain_arr.get(mid+1)):
                l=mid+1
            else:
                r=mid
        peak=l
        l=0
        r=peak
        while(l!=r):
            mid=(l+r)//2
            if(mountain_arr.get(mid)<target):
                l=mid+1
            else:
                r=mid
        if(mountain_arr.get(l)==target):
            return l
        l=peak+1
        r=n-1
        while(l!=r):
            mid=(l+r)//2
            if(mountain_arr.get(mid)>target):
                l=mid+1
            else:
                r=mid
        if(mountain_arr.get(l)==target):
            return l
        return -1