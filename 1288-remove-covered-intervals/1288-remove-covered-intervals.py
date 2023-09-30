class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res=len(intervals)
        maxlen=0
        new=sorted(intervals,key=lambda x:(x[0],-x[1]))
        for i in range(len(intervals)):
            if(new[i][1]<=maxlen):
                res-=1
            else:
                maxlen=new[i][1]
        return res