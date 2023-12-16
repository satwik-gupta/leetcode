class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        if(len(s)!=len(t)):
            return False
        for i in t:
            if(i in hashmap):
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for i in s:
            if(i in hashmap and hashmap[i]!=0):
                hashmap[i]-=1
            else:
                return False
        return True