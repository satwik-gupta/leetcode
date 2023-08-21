class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            if(len(s)%(i+1)==0):
                res=s[:i+1]
                rep=int(len(s)//(i+1))
                if((res*rep)==s and rep!=1):
                    return True
            else:
                continue
        return False
                