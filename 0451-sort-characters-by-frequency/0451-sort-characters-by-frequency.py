class Solution:
    def frequencySort(self, s: str) -> str:
        hm={}
        a=""
        for i in s:
            if i in hm:
                hm[i]+=1
            else:
                hm[i]=1
        hm=sorted(hm.items(), key = lambda x: x[1], reverse =True)
        for i in range(len(hm)):
                a+=hm[i][0]*hm[i][1]
        return a