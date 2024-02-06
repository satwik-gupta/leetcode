class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        res=[]
        for i in strs:
            arr=[0]*26
            for j in i:
                arr[ord(j)-97]+=1
            arr=tuple(arr)
            if(arr not in d):
                d[arr]=[i]
            else:
                d[arr].append(i)
        for i in d:
            res.append(d[i])
        return res