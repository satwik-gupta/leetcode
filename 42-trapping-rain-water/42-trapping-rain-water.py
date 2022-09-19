class Solution:
    def trap(self, height: List[int]) -> int:
        if(len(height)<=2):
            return 0
        i=0
        j=len(height)-1
        lmax=height[0]
        rmax=height[-1]
        trap=0
        while(i<j):
            if(height[i]>lmax):
                lmax=height[i]
            elif(height[j]>rmax):
                rmax=height[j]
            if(lmax<=rmax):
                trap+=lmax-height[i]
                i+=1
            else:
                trap+=rmax-height[j]
                j-=1
        return trap
            