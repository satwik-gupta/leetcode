class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hm={}
        for i in range(len(arr)):
            x=arr[i]/2
            if((arr[i]*2) in hm or(x==(arr[i]//2) and x in hm)):
                return True
            else:
                hm[arr[i]]=arr[i]
        return False