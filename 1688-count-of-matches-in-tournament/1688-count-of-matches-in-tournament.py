class Solution:
    def numberOfMatches(self, n: int) -> int:
        c=0
        while(n>1):
            if(n%2==0):
                c+=n//2
                n=n//2
            elif(n%2!=0 and n>2):
                c+=(n - 1) // 2
                n=(n - 1) // 2 +1
            else:
                c+=1
                n=0
        return c