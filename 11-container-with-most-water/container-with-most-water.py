class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_amount=0
        while(l<r):
            curr_max=(min(height[l],height[r]))*(r-l)
            max_amount=max(curr_max,max_amount)
            if(height[l]>height[r]):
                r-=1
            else:
                l+=1
        return max_amount
        