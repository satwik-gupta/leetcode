class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        res=[]
        arr.sort()
        i=0
        j=1
        while(j<len(arr)):
            if(arr[i][1]>=arr[j][0]):
                arr[j][0]=start=min(arr[i][0],arr[j][0])
                arr[j][1]=end=max(arr[i][1],arr[j][1])
            else:
                res.append([arr[i][0],arr[i][1]])
            i+=1
            j+=1
        res.append([arr[-1][0],arr[-1][1]])
        return res
                