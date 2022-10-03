class Solution:
    def minCost(self, s: str, nt: List[int]) -> int:
        i=0
        j=1
        x=0
        for y in range(1,len(s)):
            if(s[i]==s[j]):
                if(nt[i]>=nt[j]):
                    x+=nt[j]
                    j+=1
                else:
                    x+=nt[i]
                    i=j
                    j+=1
                    
            else:
                i=j
                j+=1
        return x