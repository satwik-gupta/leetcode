class Solution:
    def checkIfPangram(self, s: str) -> bool:
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        hm={}
        for i in s:
            if i not in hm:
                hm[i]=1
            else:
                hm[i]+=1
        if(len(hm)==26):
            return True
        else:
            return False