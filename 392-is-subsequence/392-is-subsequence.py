class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        x=0
        while c<len(s) and x<len(t):
            if(s[c]==t[x]):
                c+=1
            x+=1
        if(len(s)==c):
            return True
        else:
            return False