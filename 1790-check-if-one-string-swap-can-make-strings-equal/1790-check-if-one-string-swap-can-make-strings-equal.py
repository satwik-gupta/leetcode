class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if(s1==s2):
            return True
        if(len(s1)!=len(s2)):
            return False
        idx=[]
        for i in range(len(s1)):
            if(s1[i]!=s2[i]):
                idx.append(i)
        if(len(idx)==2 and s1[idx[0]]==s2[idx[1]] and s1[idx[1]]==s2[idx[0]]):
            return True
        else:
            return False