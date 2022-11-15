class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        n=1
        if(num==1):
            return False
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                n+=i
                if(num//i!=i):
                    n+=num//i
        if(n==num):
            return True
        else: return False