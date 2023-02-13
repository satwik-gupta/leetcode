class Solution:
    def isThree(self, n: int) -> bool:
        if(n>2):
            c=2
            for i in range(2,int(math.sqrt(n))+1):
                if(n%i==0):
                    if(n//i==i):
                        return True
                    else:
                        return False
                
                    