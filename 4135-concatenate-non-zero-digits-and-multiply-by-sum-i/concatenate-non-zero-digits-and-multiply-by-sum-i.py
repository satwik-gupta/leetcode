class Solution:
    def sumAndMultiply(self, n: int) -> int:
        multiplier=0
        power=0
        x=0
        while n>0:
            currnum=n%10
            if currnum!=0:
                multiplier+=currnum
                x+=currnum* (10**power)
                power+=1
            n=n//10
        return x*multiplier