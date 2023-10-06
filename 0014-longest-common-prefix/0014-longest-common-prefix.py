class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs, key=len)
        l=[]
        for i in strs[0]:
            l.append(i)
        for i in range(1,len(strs)):
            j=0
            while(j<len(l)):
                if(strs[i][j]==l[j]):
                    j+=1
                else:
                    l=l[:j]
                    break
                
        return "".join(l)