import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        h=[]
        for i in range(k):
            heapq.heappush(h,(-nums[i],i))
        i=0
        j=k-1
        while(j<len(nums)):
            if(h[0][1]>=i and h[0][1]<=j):
                res.append(-h[0][0])
                i+=1
                j+=1
                if(j<len(nums)):
                    heapq.heappush(h,(-nums[j],j))
            else:
                heapq.heappop(h)
        return res