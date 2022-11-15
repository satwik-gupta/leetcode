class Solution:
    def isUgly(self, n: int) -> bool:
        if(n==1):
            return True
        for i in 2,3,5:
            while(n%i==0 and n>0):
                n=n/i
        if(n==1):
            return True
        else:
            return False